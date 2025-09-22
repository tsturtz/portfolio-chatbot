setup-db:
	python -m src.db.setup

agent:
	python app.py

help:
	@echo "Available commands:"
	@echo "  setup-db   Scrapes website data and populates ChromaDB."
	@echo "  agent      Starts the agent."