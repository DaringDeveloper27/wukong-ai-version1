# wukong-ai-version1
A local AI coding assistant for developers built with Python, Streamlit, and Ollama.

# Wukong AI — Local Coding Assistant

**A personal AI coding assistant inspired by *Black Myth: Wukong*, built to help developers learn, debug, and build**

Wukong AI is a locally running chatbot powered by Ollama and Qwen 2.5 Coder. It combines AI-powered programming assistance with persistent conversation history, long-term memory, and a dark fantasy-inspired interface.

## Features

- **Local AI Assistant** — Run a coding assistant locally using Ollama.
- **Python & C++ Support** — Get explanations, debugging help, and programming guidance.
- **Conversation History** — Create and revisit previous chats.
- **Long-Term Memory** — Save useful information that Wukong can recall across conversations.
- **SQLite Storage** — Store conversations and memories locally.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web-based user interface |
| Ollama | Local AI model runtime |
| Qwen 2.5 Coder 7B | AI coding model |
| SQLite | Conversation and memory storage |

## Getting Started

### Prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/)
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/wukong-ai.git
cd wukong-ai
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the AI model

```bash
ollama pull qwen2.5-coder:7b
```

Make sure Ollama is running before launching the application.

### 5. Launch Wukong AI

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to start chatting with Wukong.

## How Memory Works

Wukong AI uses SQLite to store conversations and saved memories. When you send a message, the application searches for relevant saved memories and supplies them as context to the AI model.

This allows Wukong to use useful information across different conversations without relying on a cloud-hosted chatbot service.

## Privacy

- AI inference runs locally through Ollama.
- Conversation history and saved memories are stored in a local SQLite database.
- Your database is not intended to be committed to GitHub.

**Note:** The interface imports Google Fonts, so font loading may require an internet connection. Ollama model downloads also require internet access.

## Project Goals

- Explore local AI application development.
- Build a practical programming assistant.
- Learn how to integrate Python, databases, and language models.
- Develop a polished, game-inspired user interface.

## Future Improvements

- [ ] Streaming AI responses
- [ ] Code syntax highlighting and improved code blocks
- [ ] Conversation search and management
- [ ] Improved relevance ranking for long-term memories
- [ ] More customization options for the interface

## License

A license has not yet been selected. Add a license if you want to specify how others may use, modify, or distribute this project.

---

*Built with Python, powered by Ollama, and inspired by the legend of the Monkey King.* 
