.PHONY: setup requirements setup-db agent help

setup: requirements
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

setup-db:
	python -m src.db.setup

agent:
	python app.py

help:
	@echo "Available commands:"
	@echo "  setup         Installs project dependencies."
	@echo "  requirements  Generates requirements.txt."
	@echo "  setup-db      Scrapes website data and populates ChromaDB."
	@echo "  agent         Starts the agent."