# Market Monitoring AI Agent

A market intelligence AI agent that monitors financial, policy, and other economic news and classifies developments as how important they are and presents the result to you accordingly.

## Features
- LangChain-based ReAct agent
- Groq LLM integration
- Real-time news ingestion
- Important vs Ignore classification
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
```
### 2. Create virtual environment
```
uv venv
.venv\Scripts\activate
```
### 3. Install dependencies
```
uv pip install -r requirements.txt
```
### 4. Set environment variables
```
setx GROQ_API_KEY "your_groq_key"
setx NEWS_API_KEY "your_newsapi_key"
```
### 5. Run the app
```
streamlit run app.py
```
## Example Prompts

Gold prices surge after US Fed signals rate cuts

Indian stock market reacts to global recession fears

Gold prices today

## Some outputs
<img width="1438" height="970" alt="Screenshot 2026-01-30 181855" src="https://github.com/user-attachments/assets/7aa39bf7-0d0c-4e14-842c-067957e40405" />
