SHELL := /usr/bin/env bash

SCRIPT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PROJECT_ROOT := $(abspath $(SCRIPT_DIR)/..)
WORK_DIR := $(PROJECT_ROOT)/work
JUPYTER_TOKEN ?= vscode-jupyter-token
DOCKER_COMPOSE ?= docker compose
SERVICE_NAME ?= jupyter
IMAGE_NAME ?= statistical-analysis-jupyter:latest

# Dockerfileビルド時に requestment.txt 経由でインストールされるパッケージ
# パッケージを追加・削除する場合は requestment.txt を編集して make build を実行すること
PACKAGES := \
	numpy \
	pandas \
	matplotlib \
	japanize-matplotlib \
	scipy \
	scikit-learn \
	requests \
	pandas-datareader \
	lxml \
	PyPDF2 \
	googletrans \
	pdfplumber \
	plotly

.PHONY: start build stop logs

start:
	@mkdir -p "$(WORK_DIR)"
	@if ! docker image inspect "$(IMAGE_NAME)" >/dev/null 2>&1; then \
		echo "Image $(IMAGE_NAME) not found. Running make build..."; \
		$(MAKE) build; \
	fi
	@cd "$(SCRIPT_DIR)" && JUPYTER_TOKEN="$(JUPYTER_TOKEN)" $(DOCKER_COMPOSE) up -d
	@echo "Jupyter URL for VS Code: http://127.0.0.1:8888/?token=$(JUPYTER_TOKEN)"

build:
	@cd "$(SCRIPT_DIR)"; \
	if docker image inspect "$(IMAGE_NAME)" >/dev/null 2>&1; then \
		echo "Removing existing image $(IMAGE_NAME)..."; \
		$(DOCKER_COMPOSE) down >/dev/null 2>&1 || true; \
		docker rmi -f "$(IMAGE_NAME)" >/dev/null; \
	fi; \
	echo "Building image $(IMAGE_NAME)..."; \
	$(DOCKER_COMPOSE) build $(SERVICE_NAME)

stop:
	@cd "$(SCRIPT_DIR)" && $(DOCKER_COMPOSE) down

logs:
	@cd "$(SCRIPT_DIR)" && $(DOCKER_COMPOSE) logs -f $(SERVICE_NAME)
