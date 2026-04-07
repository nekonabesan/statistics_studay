SHELL := /usr/bin/env bash

SCRIPT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PROJECT_ROOT := $(abspath $(SCRIPT_DIR)/..)
WORK_DIR := $(PROJECT_ROOT)/work
JUPYTER_TOKEN ?= vscode-jupyter-token
DOCKER_COMPOSE ?= docker compose
SERVICE_NAME ?= jupyter
IMAGE_NAME ?= statistical-analysis-jupyter:latest

# 依存関係は pyproject.toml / uv.lock で管理する
# 追加・更新時は pyproject.toml を編集し、make lock 実行後に make build する

.PHONY: start build stop logs lock

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

lock:
	@cd "$(SCRIPT_DIR)"; \
	if ! docker image inspect "$(IMAGE_NAME)" >/dev/null 2>&1; then \
		echo "Image $(IMAGE_NAME) not found. Running make build..."; \
		$(MAKE) build; \
	fi; \
	docker run --rm -v "$$PWD:/work" -w /work "$(IMAGE_NAME)" uv lock
