FROM jupyter/base-notebook:latest

# Python パッケージ定義をコピーして一括インストール
COPY requestment.txt /tmp/requestment.txt

RUN pip install --no-cache-dir -r /tmp/requestment.txt

# コンテナシェルから追加インストールしやすいように明示
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
