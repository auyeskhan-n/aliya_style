# Kaspi Price List Generator Makefile

.PHONY: help install test validate deploy clean setup

help: ## Show this help message
	@echo "Kaspi Price List Generator - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install Python dependencies
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

test: ## Test with sample data
	. venv/bin/activate && python fetch_and_convert.py --sample

validate: ## Validate generated XML
	. venv/bin/activate && python validate_xml.py

deploy: ## Prepare files for deployment
	. venv/bin/activate && python deploy.py

setup: ## Run interactive setup
	. venv/bin/activate && python setup.py

clean: ## Clean generated files
	rm -f price.xml
	rm -rf gh-pages/
	rm -rf venv/

all: install test validate ## Install, test, and validate
	@echo "✅ All tasks completed successfully!"

# Development targets
dev-test: ## Quick development test
	. venv/bin/activate && python fetch_and_convert.py --sample && python validate_xml.py

# GitHub Actions simulation
ci-test: ## Simulate GitHub Actions workflow
	@echo "🔧 Setting up Python environment..."
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	@echo "📊 Fetching data and generating XML..."
	. venv/bin/activate && python fetch_and_convert.py --sample
	@echo "✅ Validating XML..."
	. venv/bin/activate && python validate_xml.py
	@echo "🚀 Preparing for deployment..."
	. venv/bin/activate && python deploy.py
	@echo "✅ CI simulation completed successfully!"
