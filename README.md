---
title: Portfolio Chatbot
emoji: 🤖
colorFrom: yellow
colorTo: green
sdk: docker
app_file: app.py
---

#### HuggingFace config:
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Portfolio Chatbot

A very lightweight chatbot using the following technologies to be able to answer questions about my professional experience:
- Python
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [LangChain](https://www.langchain.com/)
- [Chroma DB](https://www.trychroma.com/)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- Gemini model: `gemini-2.5-flash-lite` with RAG (resource augmented generation)

### Hosted on Hugging Face Spaces:
GET: https://tsturtz-portfolio-chatbot.hf.space/health
POST: https://tsturtz-portfolio-chatbot.hf.space/prompt

## Getting Started

```sh
make help
```

## TODO
- Defend against bots (captcha)
- Add escape button to close the chat window.
- Handle rate limiting in UI (already implemented on the server)
- Look into using small model
