# 🧠 Terminal LLM Chatbot using LangChain

This is a simple terminal-based chatbot built with [LangChain](https://www.langchain.com/) that allows users to interact with a Large Language Model (LLM) directly from the command line. Users can choose which model they want to talk to, send a message, and receive a response in real time.

## 📌 Features

- Interactive chat with an LLM from your terminal.
- Select from multiple models (e.g., OpenAI, anthropic and google.).
- Lightweight and easy to run.

## 🚀 Requirements

- Python 3.8+
- [LangChain](https://python.langchain.com/)
- An API key for the LLM provider you want to use (e.g., OpenAI API key)

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/MustaphaMensouri/chat_with_LLM_from_termnial.git
cd chat_with_LLM_from_termnial

poetry install

mv .env.example .env

# add your keys to .env

python chat_model/chat_model1.py 
```
