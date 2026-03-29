#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

import pdfplumber


DEFAULT_TABLE_SETTINGS = {
	"horizontal_strategy": "text",
	"vertical_strategy": "lines",
	"intersection_tolerance": 5,
	"snap_tolerance": 3,
	"join_tolerance": 3,
	"text_x_tolerance": 2,
	"text_y_tolerance": 3,
}

MATH_PATTERN = re.compile(
	r"("  # equation operators or common math keywords/symbols
	r"[=±×÷∑∏∫√∞≈≠≤≥∂∆^_]|"
	r"\b(sin|cos|tan|log|ln|exp|max|min|arg|min|lim|cov|var|E)\b|"
	r"\b[a-zA-Z]\s*=\s*|"
	r"\([^\)]*\)\s*=|"
	r"\d\s*/\s*\d"
	r")"
)


@dataclass
class TextBlock:
	top: float
	text: str


@dataclass
class TableBlock:
	top: float
	rows: List[List[str]]


Block = TextBlock | TableBlock


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Convert an arbitrary PDF file to Markdown using pdfplumber."
	)
	parser.add_argument("input_pdf", help="Path to input PDF file")
	parser.add_argument(
		"-o",
		"--output",
		help="Path to output Markdown file. Defaults to <input>.md",
	)
	parser.add_argument(
		"--no-page-separators",
		action="store_true",
		help="Do not emit page separators and page headings.",
	)
	return parser.parse_args()


def normalize_whitespace(text: str) -> str:
	text = text.replace("\u00a0", " ")
	text = re.sub(r"[ \t]+", " ", text)
	text = re.sub(r"\n{3,}", "\n\n", text)
	return text.strip()


def sanitize_cell(cell: object) -> str:
	if cell is None:
		return ""
	value = str(cell).replace("\u00a0", " ")
	value = value.replace("|", r"\|")
	value = re.sub(r"\s+", " ", value).strip()
	return value


def looks_like_formula(line: str) -> bool:
	stripped = line.strip()
	if not stripped:
		return False
	if len(stripped) > 160:
		return False
	if stripped.startswith(("Figure", "Table", "Source", "Note")):
		return False

	symbol_count = sum(1 for ch in stripped if ch in "=+-*/^_()[]{}%<>")
	digit_count = sum(ch.isdigit() for ch in stripped)
	alpha_count = sum(ch.isalpha() for ch in stripped)

	if MATH_PATTERN.search(stripped):
		return True
	if symbol_count >= 2 and digit_count >= 1 and alpha_count <= max(18, len(stripped) // 2):
		return True
	return False


def to_markdown_table(rows: List[List[str]]) -> str:
	cleaned_rows = [[sanitize_cell(cell) for cell in row] for row in rows if row is not None]
	cleaned_rows = [row for row in cleaned_rows if any(cell for cell in row)]
	if not cleaned_rows:
		return ""

	max_cols = max(len(row) for row in cleaned_rows)
	normalized_rows = [row + [""] * (max_cols - len(row)) for row in cleaned_rows]

	header = normalized_rows[0]
	body = normalized_rows[1:] if len(normalized_rows) > 1 else []

	lines = []
	lines.append("| " + " | ".join(header) + " |")
	lines.append("| " + " | ".join([":--"] * max_cols) + " |")
	for row in body:
		lines.append("| " + " | ".join(row) + " |")
	return "\n".join(lines)


def merge_text_lines(lines: Iterable[dict]) -> List[TextBlock]:
	blocks: List[TextBlock] = []
	current_text: List[str] = []
	current_top: float | None = None
	previous_top: float | None = None

	for line in lines:
		text = normalize_whitespace(line.get("text", ""))
		if not text:
			continue

		top = float(line.get("top", 0.0))
		if current_top is None:
			current_top = top
			current_text = [text]
			previous_top = top
			continue

		same_paragraph = previous_top is not None and abs(top - previous_top) <= 14
		previous_line = current_text[-1] if current_text else ""
		previous_formula = looks_like_formula(previous_line)
		current_formula = looks_like_formula(text)

		if same_paragraph and previous_formula == current_formula:
			current_text.append(text)
		else:
			blocks.append(TextBlock(top=current_top, text="\n".join(current_text)))
			current_top = top
			current_text = [text]

		previous_top = top

	if current_text and current_top is not None:
		blocks.append(TextBlock(top=current_top, text="\n".join(current_text)))

	return blocks


def extract_blocks(page: pdfplumber.page.Page) -> List[Block]:
	tables = page.find_tables(table_settings=DEFAULT_TABLE_SETTINGS)

	text_region = page
	for table in tables:
		text_region = text_region.outside_bbox(table.bbox)

	text_lines = text_region.extract_text_lines() or []
	blocks: List[Block] = merge_text_lines(text_lines)

	for table in tables:
		extracted_rows = table.extract()
		if extracted_rows:
			blocks.append(TableBlock(top=float(table.bbox[1]), rows=extracted_rows))

	blocks.sort(key=lambda item: item.top)
	return blocks


def render_text_block(text: str) -> str:
	lines = [normalize_whitespace(line) for line in text.splitlines()]
	lines = [line for line in lines if line]
	if not lines:
		return ""

	if all(looks_like_formula(line) for line in lines):
		return "$$\n" + "\n".join(lines) + "\n$$"

	rendered: List[str] = []
	math_buffer: List[str] = []

	def flush_math_buffer() -> None:
		if math_buffer:
			rendered.append("$$\n" + "\n".join(math_buffer) + "\n$$")
			math_buffer.clear()

	for line in lines:
		if looks_like_formula(line):
			math_buffer.append(line)
		else:
			flush_math_buffer()
			rendered.append(line)

	flush_math_buffer()
	return "\n\n".join(rendered)


def render_page(page_number: int, blocks: List[Block], include_page_header: bool) -> str:
	rendered: List[str] = []
	if include_page_header:
		rendered.append(f"## Page {page_number}")

	for block in blocks:
		if isinstance(block, TextBlock):
			text_md = render_text_block(block.text)
			if text_md:
				rendered.append(text_md)
		else:
			table_md = to_markdown_table(block.rows)
			if table_md:
				rendered.append(table_md)

	return "\n\n".join(rendered).strip()


def convert_pdf_to_markdown(input_pdf: Path, output_md: Path, include_page_header: bool) -> None:
	page_sections: List[str] = []

	with pdfplumber.open(input_pdf) as pdf:
		for page_number, page in enumerate(pdf.pages, start=1):
			blocks = extract_blocks(page)
			page_md = render_page(page_number, blocks, include_page_header)
			if page_md:
				page_sections.append(page_md)
			elif include_page_header:
				page_sections.append(f"## Page {page_number}\n\n(No extractable content)")

	document_title = input_pdf.stem.replace("_", " ")
	output = [f"# {document_title}"]
	if page_sections:
		output.append("\n\n---\n\n".join(page_sections))

	output_md.parent.mkdir(parents=True, exist_ok=True)
	output_md.write_text("\n\n".join(output).strip() + "\n", encoding="utf-8")


def main() -> None:
	args = parse_args()
	input_pdf = Path(args.input_pdf).expanduser().resolve()
	if not input_pdf.exists():
		raise FileNotFoundError(f"Input PDF not found: {input_pdf}")

	output_md = (
		Path(args.output).expanduser().resolve()
		if args.output
		else input_pdf.with_suffix(".md")
	)

	convert_pdf_to_markdown(
		input_pdf=input_pdf,
		output_md=output_md,
		include_page_header=not args.no_page_separators,
	)
	print(f"Wrote Markdown to {output_md}")


if __name__ == "__main__":
	main()
