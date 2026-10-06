# 🔬 InsightFlow-AI

> **Search → Scrape → Write → Critique**

InsightFlow-AI is an AI-powered research agent that automates the process of researching a topic, gathering information from the web, generating a structured report, and critically evaluating the result.

The project uses a multi-agent workflow built with **LangChain, Groq, Tavily, BeautifulSoup, and Streamlit**.

---

## ✨ Features

- 🔎 Web search for recent and relevant information
- 📄 Webpage scraping for deeper research
- 🤖 Multi-agent research workflow
- ✍️ Automated report generation
- 🧐 AI-powered report critique and scoring
- 📊 Interactive Streamlit interface
- 🔐 Environment-based API key management

---

## 🏗️ Architecture

```text
User Topic
    │
    ▼
┌──────────────┐
│ Search Agent │ ──── Tavily
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Reader Agent │ ──── Web Scraping
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Writer    │ ──── Research Report
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Critic    │ ──── Score + Feedback
└──────────────┘
```

### Workflow

1. **Search Agent** finds relevant web sources using Tavily.
2. **Reader Agent** selects a useful source and extracts its content.
3. **Writer** generates a structured research report.
4. **Critic** evaluates the report and provides feedback.

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq**
- **Tavily**
- **BeautifulSoup**
- **Requests**
- **Streamlit**
- **python-dotenv**

---

## 📂 Project Structure

```text
InsightFlow-AI/
│
├── app.py                 # Streamlit UI
├── pipeline.py            # Research pipeline
├── agents.py              # Agents and LLM chains
│
├── tools/
│   ├── __init__.py
│   └── tools.py           # Search and scraping tools
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/InsightFlow-AI.git
cd InsightFlow-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🚀 Example

Enter a research topic such as:

```text
Latest advancements in Generative AI
```

InsightFlow-AI will:

```text
Search the Web
      ↓
Read Relevant Sources
      ↓
Generate Report
      ↓
Critique Report
```

The UI provides three sections:

- 📝 **Final Report**
- 🧐 **Critic Feedback**
- 🔎 **Search Results**

---

## 👩‍💻 Author

**Naina Dugar**

Computer Science & Data Analytics Student  
Interested in **AI Engineering, Agentic AI, and Full-Stack Development**.
