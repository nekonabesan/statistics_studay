FROM jupyter/base-notebook:latest

# よく使う Python パッケージを事前インストール
RUN pip install --no-cache-dir \
	numpy \
	pandas \
	matplotlib \
	scipy \
	scikit-learn

# コンテナシェルから追加インストールしやすいように明示
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
