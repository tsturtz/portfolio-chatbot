---
title: Portfolio Chatbot
emoji: 🤖
colorFrom: yellow
colorTo: green
sdk: docker
app_file: app.py
---

# Portfolio Chatbot

A very lightweight chatbot using the following technologies to be able to answer questions about my professional experience:
- Python
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [LangChain](https://www.langchain.com/)
- [Chroma DB](https://www.trychroma.com/)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

## Install
```sh
python -m venv .venv
source .venv/bin/activate # or Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```sh
python app.py
```

## TODO
- Dockerize
- Set up Hugging Face Spaces
- Integrate with portfolio website