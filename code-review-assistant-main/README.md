# GenAI-Code-Review-Assistant

An AI-powered code review application built with **FastAPI** and **Anthropic Claude** that analyzes Python code and provides structured feedback on bugs, security issues, code quality, and improvement suggestions.

---

## ✨ Features

- 🐞 Detect logical bugs and potential runtime issues
- 🔒 Identify common security vulnerabilities
- 📝 Review code quality, readability, and best practices
- 💡 Generate actionable improvement suggestions
- ⚡ FastAPI REST API backend
- 🎨 Lightweight HTML, CSS, and JavaScript frontend
- 🤖 AI-powered analysis using Claude Sonnet

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python, FastAPI, Pydantic |
| Frontend | HTML, CSS, Vanilla JavaScript |
| AI | Anthropic Claude Sonnet |
| Deployment | Render (Backend), Static HTML (Frontend) |

---

## 📂 Project Structure

```text
GenAI-Code-Review-Assistant/
│
├── backend/
│   ├── main.py              # FastAPI application
│   ├── reviewer.py          # Claude API integration
│   ├── requirements.txt
│   ├── .env.example         # Example environment variables
│   └── .env                 # Local environment variables (ignored by Git)
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

## 📋 Prerequisites

Before running the project, ensure you have:

- Python 3.10 or later
- Git
- Anthropic API Key

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mekalakarthik05/GenAI-Code-Review-Assistant.git
cd GenAI-Code-Review-Assistant
```

### 2. Create a Virtual Environment

```bash
cd backend

python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file.

**Windows**

```cmd
copy .env.example .env
```

**macOS/Linux**

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your Anthropic API key.

```env
ANTHROPIC_API_KEY=your_api_key_here
MODEL_NAME=claude-sonnet-4-20250514
USE_MOCK=false
```

### 5. Start the Backend

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

### 6. Launch the Frontend

Open:

```
frontend/index.html
```

in your browser.

---

## 💻 Usage

1. Paste Python code into the editor.
2. Click **Review My Code** (or press **Ctrl + Enter**).
3. Receive AI-generated feedback organized into:
   - 🐞 Bugs
   - 🔒 Security
   - 📝 Code Quality
   - 💡 Suggestions

---

## 🔐 Environment Variables

This project uses environment variables for sensitive configuration.

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `MODEL_NAME` | Claude model to use |
| `USE_MOCK` | Enable mock responses for development |


---

## 📚 What I Learned

This project helped me gain hands-on experience with:

- Prompt engineering for structured LLM outputs
- Building REST APIs using FastAPI
- Pydantic request and response validation
- Integrating Anthropic Claude APIs
- Parsing and validating LLM responses
- Error handling and API design
- Frontend-backend communication using Fetch API
- CORS configuration for local development
- Secure configuration management using environment variables

---

## 🚀 Future Improvements

- Support multiple programming languages
- Streaming AI responses
- Syntax highlighting editor (Monaco)
- File upload support
- Downloadable review reports
- Authentication and rate limiting
- Docker deployment
- Unit and integration tests

---

## 👨‍💻 Author

**Karthik Mekala**

GitHub: https://github.com/mekalakarthik05

LinkedIn: https://www.linkedin.com/in/karthik-mekala-k05
