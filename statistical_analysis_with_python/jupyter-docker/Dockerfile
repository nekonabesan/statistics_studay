FROM jupyter/base-notebook:latest

USER root

# uv をインストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# matplotlib の日本語表示用フォントをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
	fonts-noto-cjk \
	fonts-ipafont-gothic \
	fonts-ipaexfont-gothic \
	fonts-ipaexfont-mincho \
	fontconfig \
	&& fc-cache -f -v \
	&& rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# uvプロジェクト定義とロックファイルをコピーして一括インストール
COPY pyproject.toml uv.lock /tmp/uvproj/

RUN cd /tmp/uvproj \
	&& uv export --frozen --no-dev --format requirements-txt -o /tmp/requirements.lock.txt \
	&& uv pip install --system -r /tmp/requirements.lock.txt

# matplotlib のフォントキャッシュを再生成し、IPAexGothic が見えることを確認
RUN rm -rf /home/${NB_USER}/.cache/matplotlib \
	&& python -c "import sys, matplotlib.font_manager as fm; names={f.name for f in fm.fontManager.ttflist}; ok=('IPAexGothic' in names or 'IPAex Gothic' in names); print('IPAexGothic available:', ok); sys.exit(0 if ok else 1)" \
	&& python -c "import matplotlib; print('matplotlib', matplotlib.__version__)"
