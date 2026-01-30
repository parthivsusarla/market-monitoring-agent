# Market Monitoring AI Agent

A market intelligence AI agent that monitors financial, policy, and macroeconomic news and classifies developments as **IMPORTANT** or **IGNORE** based on potential market impact.

## Features
- LangChain-based ReAct agent
- Groq LLM integration
- Real-time news ingestion
- IMPORTANT vs IGNORE classification
- Fault-tolerant execution with retries
- Streamlit frontend

## Tech Stack
- Python
- LangChain
- Groq API
- NewsAPI
- Streamlit
- uv (environment management)

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/parthivsusarla/market-agent.git
cd market-agent

### 2. Create virtual environment
uv venv
.venv\Scripts\activate

### 3. Install dependencies
uv pip install -r requirements.txt

### 4. Set environment variables
setx GROQ_API_KEY "your_groq_key"
setx NEWS_API_KEY "your_newsapi_key"

### 5. Run the app
streamlit run app.py

## 
Example Prompts

Gold prices surge after US Fed signals rate cuts

Indian stock market reacts to global recession fears

Gold prices today