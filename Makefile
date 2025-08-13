.PHONY: help install install-dev test test-unit test-integration lint format clean build publish

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	pip install -e .

install-dev: ## Install the package with development dependencies
	pip install -e ".[dev]"

test: ## Run unit tests only (safe for CI)
	pytest -m "not integration"

test-unit: ## Run unit tests only
	pytest -m "not integration"

test-integration: ## Run integration tests only (requires real server)
	pytest -m "integration"

test-all: ## Run all tests including integration (requires real server)
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=gotty_py --cov-report=html --cov-report=term

lint: ## Run linting checks
	flake8 tests examples
	# mypy .  # Temporarily disabled due to module path issues

format: ## Format code with black and isort
	black tests examples
	isort tests examples

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	python -m build

publish: ## Publish to PyPI (requires twine)
	twine upload dist/*

check: ## Run all checks (lint, test, format)
	make lint
	make test-unit
	make format

example-basic: ## Run basic usage example
	python examples/basic_usage.py

example-advanced: ## Run advanced usage example
	python examples/advanced_usage.py
