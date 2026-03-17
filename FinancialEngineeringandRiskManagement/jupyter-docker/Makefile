SHELL := /usr/bin/env bash

SCRIPT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PROJECT_ROOT := $(abspath $(SCRIPT_DIR)/..)
WORK_DIR := $(PROJECT_ROOT)/work

IMAGE_NAME ?= ferm-jupyter:latest
CONTAINER_NAME ?= jupyter
JUPYTER_TOKEN ?= vscode-jupyter-token

.PHONY: start stop logs install innstall

# Allows: make install numpy
ifneq ($(filter install innstall,$(MAKECMDGOALS)),)
  MODULE_FROM_GOAL := $(word 2,$(MAKECMDGOALS))
  ifneq ($(MODULE_FROM_GOAL),)
    $(eval $(MODULE_FROM_GOAL):;@:)
  endif
endif

start:
	@mkdir -p "$(WORK_DIR)"
	@if docker ps -a --format '{{.Names}}' | grep -q "^$(CONTAINER_NAME)$$"; then \
		docker rm -f "$(CONTAINER_NAME)" >/dev/null; \
	fi
	@docker build -t "$(IMAGE_NAME)" "$(SCRIPT_DIR)"
	@docker run -d \
		--name "$(CONTAINER_NAME)" \
		-p 8888:8888 \
		-v "$(WORK_DIR):/home/jovyan/work" \
		"$(IMAGE_NAME)" \
		start-notebook.sh \
		--NotebookApp.token="$(JUPYTER_TOKEN)" \
		--NotebookApp.password='' \
		--NotebookApp.allow_origin='*'
	@echo "Jupyter URL for VS Code: http://127.0.0.1:8888/?token=$(JUPYTER_TOKEN)"

stop:
	@if docker ps -a --format '{{.Names}}' | grep -q "^$(CONTAINER_NAME)$$"; then \
		docker stop "$(CONTAINER_NAME)" >/dev/null; \
		docker rm "$(CONTAINER_NAME)" >/dev/null; \
		echo "Stopped and removed $(CONTAINER_NAME)"; \
	else \
		echo "Container $(CONTAINER_NAME) is not running."; \
	fi

logs:
	@docker logs -f "$(CONTAINER_NAME)"

install:
	@module="$(or $(MODULE),$(MODULE_FROM_GOAL))"; \
	if [ -z "$$module" ]; then \
		echo "Usage: make install <module_name>"; \
		exit 1; \
	fi; \
	if ! docker ps --format '{{.Names}}' | grep -q "^$(CONTAINER_NAME)$$"; then \
		echo "Container $(CONTAINER_NAME) is not running. Run 'make start' first."; \
		exit 1; \
	fi; \
	docker exec -i "$(CONTAINER_NAME)" pip install --no-cache-dir "$$module"

innstall: install
