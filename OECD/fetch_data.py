#!/usr/bin/env python3
"""
OECD データダウンロードスクリプト
OECD SDMX API v2.1 から 4 種のデータを取得し OECD/data/ に CSV として保存。

使い方:
    python fetch_data.py
"""

import csv
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

# ─── 設定 ─────────────────────────────────────────────────────────────────────
BASE_URL = "https://sdmx.oecd.org/public/rest/data"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "Accept": "application/vnd.sdmx.genericdata+xml; charset=utf-8; version=2.1"
}
# SDMX 2.1 名前空間
NS_GEN = "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic"

SLEEP_BETWEEN_REQUESTS = 5  # API レート制限対策（秒）


# ─── 共通関数 ──────────────────────────────────────────────────────────────────
def fetch_xml(flow_ref: str, key: str, start_period: str, end_period: str,
              timeout: int = 360) -> bytes:
    url = f"{BASE_URL}/{flow_ref}/{key}"
    params = {
        "startPeriod": start_period,
        "endPeriod": end_period,
        "detail": "dataonly",
    }
    print(f"  GET {url}")
    print(f"      ?startPeriod={start_period}&endPeriod={end_period}&detail=dataonly")
    resp = requests.get(url, params=params, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    size_kb = len(resp.content) / 1024
    print(f"  {resp.status_code} OK  ({size_kb:,.1f} KB)")
    return resp.content


def parse_sdmx(xml_bytes: bytes) -> list:
    """SDMX GenericData XML をフラット dict リストに変換"""
    root = ET.fromstring(xml_bytes)
    records = []
    series_count = 0

    for series in root.iter(f"{{{NS_GEN}}}Series"):
        series_count += 1
        # SeriesKey から次元値取得
        key_map = {}
        sk = series.find(f"{{{NS_GEN}}}SeriesKey")
        if sk is not None:
            for v in sk.findall(f"{{{NS_GEN}}}Value"):
                key_map[v.get("id", "")] = v.get("value", "")

        # 観測値
        for obs in series.findall(f"{{{NS_GEN}}}Obs"):
            rec = dict(key_map)
            od = obs.find(f"{{{NS_GEN}}}ObsDimension")
            ov = obs.find(f"{{{NS_GEN}}}ObsValue")
            rec["TIME_PERIOD"] = od.get("value", "") if od is not None else ""
            rec["OBS_VALUE"]   = ov.get("value", "") if ov is not None else ""
            records.append(rec)

    print(f"  Series: {series_count:,}  Obs: {len(records):,}")
    return records


def to_csv(records: list, filename: str) -> None:
    if not records:
        print(f"  !! データなし: {filename}")
        return
    path = DATA_DIR / filename
    # 全レコードのキー順序を保持して収集
    cols = list(dict.fromkeys(k for r in records for k in r))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(records)
    size_kb = path.stat().st_size / 1024
    print(f"  ✓ {path.name}  ({len(records):,} 行, {size_kb:,.1f} KB)")


def run(name: str, flow_ref: str, key: str,
        start: str, end: str, filename: str) -> list:
    print(f"\n{'─'*60}")
    print(f"  {name}")
    print(f"  flow_ref : {flow_ref}")
    print(f"  key      : {key}  (次元数={len(key.split('.'))})")
    try:
        xml_bytes = fetch_xml(flow_ref, key, start, end)
        records = parse_sdmx(xml_bytes)
        to_csv(records, filename)
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        return records
    except requests.HTTPError as e:
        body = e.response.text[:600]
        print(f"  !! HTTP {e.response.status_code}: {body}")
        return []
    except Exception as e:
        import traceback
        print(f"  !! {type(e).__name__}: {e}")
        traceback.print_exc()
        return []


# ─────────────────────────────────────────────────────────────────────────────
# 1. GDP（年次・実質）
# ─────────────────────────────────────────────────────────────────────────────
# DSD_NAMAIN10 軸順（12 次元）:
#   FREQ(1) . REF_AREA(2) . SECTOR(3) . COUNTERPART_SECTOR(4) . TRANSACTION(5)
#   . INSTR_ASSET(6) . ACTIVITY(7) . EXPENDITURE(8) . UNIT_MEASURE(9)
#   . PRICE_BASE(10) . TRANSFORMATION(11) . TABLE_IDENTIFIER(12)
#
# key: A....B1GQ.......
#  A=FREQ=年次, ....=REF_AREA~COUNTERPART_SECTOR ワイルドカード,
#  B1GQ=TRANSACTION(GDP), .......=INSTR_ASSET~TABLE_IDENTIFIER 全ワイルドカード
#  ※このフローの PRICE_BASE=LR(連鎖参照年価格)・UNIT_MEASURE=USD_PPP は固定値のみ存在
# → split(".") = 12要素 ✓
# ─────────────────────────────────────────────────────────────────────────────
r_gdp = run(
    name     = "GDP（年次・リビジョンなし B1GQ, PRICE_BASE=LR, UNIT=USD_PPP）",
    flow_ref = "OECD.SDD.NAD,DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_VPVOB,2.0",
    key      = "A....B1GQ.......",
    start    = "1970",
    end      = "2025",
    filename = "gdp_annual.csv",
)

# ─────────────────────────────────────────────────────────────────────────────
# 2. 鉱工業生産指数（IIP）月次
# ─────────────────────────────────────────────────────────────────────────────
# DSD_STES 軸順（9 次元）:
#   REF_AREA(1) . FREQ(2) . MEASURE(3) . UNIT_MEASURE(4) . ACTIVITY(5)
#   . ADJUSTMENT(6) . TRANSFORMATION(7) . TIME_HORIZ(8) . METHODOLOGY(9)
#
# key: .M.PRVM......
#  .=REF_AREA ワイルドカード, M=FREQ=月次, PRVM=MEASURE=生産量指数,
#  ......=UNIT_MEASURE~METHODOLOGY 全ワイルドカード（UNIT=IX, TRANSFORMATION=_Z が固定）
#  ACTIVITY: BTE(全産業建設含), C(製造業), D(電力等), F(建設), MIG_NRG(産業群)
# → split(".") = 9要素 ✓
# ─────────────────────────────────────────────────────────────────────────────
r_iip = run(
    name     = "鉱工業生産指数（IIP）月次 MEASURE=PRVM, 全産業",
    flow_ref = "OECD.SDD.STES,DSD_STES@DF_INDSERV,4.3",
    key      = ".M.PRVM......",
    start    = "1970-01",
    end      = "2025-12",
    filename = "iip_monthly.csv",
)

# ─────────────────────────────────────────────────────────────────────────────
# 3. 労働生産性（PDB 年次）
# ─────────────────────────────────────────────────────────────────────────────
# DSD_PDB 軸順（9 次元）:
#   REF_AREA(1) . FREQ(2) . MEASURE(3) . ACTIVITY(4) . UNIT_MEASURE(5)
#   . PRICE_BASE(6) . TRANSFORMATION(7) . ASSET_CODE(8) . CONVERSION_TYPE(9)
#
# key: .A.......
#  .=REF_AREA ワイルドカード, A=FREQ=年次, .......=残6次元ワイルドカード
# → split(".") = 9要素 ✓
# ─────────────────────────────────────────────────────────────────────────────
r_pdb_a = run(
    name     = "労働生産性（PDB 年次 DF_PDB_LV）",
    flow_ref = "OECD.SDD.TPS,DSD_PDB@DF_PDB_LV,1.0",
    key      = ".A.......",
    start    = "1970",
    end      = "2025",
    filename = "labor_productivity_annual.csv",
)

# ─────────────────────────────────────────────────────────────────────────────
# 4. 労働生産性・単位労働コスト（PDB 四半期）
# ─────────────────────────────────────────────────────────────────────────────
# 同 DSD_PDB 構造、DF_PDB_ULC_Q を使用
# key: .Q.......
#  .=REF_AREA ワイルドカード, Q=FREQ=四半期, .......=残ワイルドカード
# → split(".") = 9要素 ✓
# ─────────────────────────────────────────────────────────────────────────────
r_pdb_q = run(
    name     = "労働生産性・ULC（PDB 四半期 DF_PDB_ULC_Q）",
    flow_ref = "OECD.SDD.TPS,DSD_PDB@DF_PDB_ULC_Q,1.0",
    key      = ".Q.......",
    start    = "1970-Q1",
    end      = "2025-Q4",
    filename = "labor_productivity_ulc_quarterly.csv",
)

# ─────────────────────────────────────────────────────────────────────────────
# サマリ
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("=== 取得完了サマリ ===")
for label, rec in [
    ("GDP（年次・本値 USD_PPP）",          r_gdp),
    ("IIP（鉱工業生産指数・月次）",                r_iip),
    ("PDB 労働生産性（年次）",     r_pdb_a),
    ("PDB 労働生産性・ULC（四半期）", r_pdb_q),
]:
    status = f"{len(rec):,} 件" if rec else "!! データなし / エラー"
    print(f"  {label:<26}: {status}")

print(f"\n保存先: {DATA_DIR}")
