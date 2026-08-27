# 🤖 Autonomous Business Analyst AI

<p align="center">
  <strong>Turn one business idea into a professional, data-driven business plan using autonomous AI agents.</strong>
</p>

<p align="center">
  <a href="https://autonomous-buisness-analyst.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Streamlit-FF4B4B?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/jatinkumar4148/Autonomous-Buisness-Analyst">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

<p align="center">
  <a href="https://autonomous-buisness-analyst.streamlit.app/">🌐 Open Live Application</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/jatinkumar4148/Autonomous-Buisness-Analyst">📦 View Source Code</a>
</p>

---

## 🚀 [Live Demo]([url](https://autonomous-buisness-analyst.streamlit.app/))

### [Open Autonomous Business Analyst AI →](https://autonomous-buisness-analyst.streamlit.app/)

Enter a simple idea such as:

> **I want to open a coffee shop in Delhi**

The system analyzes the idea through five specialized AI dimensions and produces a structured business plan.

---

## ✨ About the Project

**Autonomous Business Analyst AI** is a multi-agent AI application designed to transform a raw business idea into a structured business analysis and actionable business plan.

The application combines:

- 🧠 Mistral AI
- 🔗 LangChain
- 🔄 LangGraph
- 📚 RAG
- ⚡ FAISS
- 🎨 Streamlit

---

# 🏗️ System Architecture

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/cdd3d99d-5c34-4377-8680-6525c7266140"
    alt="Autonomous Business Analyst AI System Architecture"
    width="100%"
  />
</p>

### 🔄 Workflow

**Business Idea → RAG Knowledge Base → Five Specialized AI Agents → LangGraph Orchestrator → Synthesizer → Complete Business Plan**

### What happens?

1. 💡 **Business Idea** — User provides the business concept.
2. 📚 **RAG Knowledge Base** — Relevant business knowledge is retrieved.
3. 🤖 **Five AI Agents** — The idea is analyzed from five different business perspectives.
4. 🔄 **LangGraph Orchestrator** — Coordinates the agent workflow and shared state.
5. 🧠 **Synthesizer** — Combines the individual analyses.
6. 📄 **Complete Business Plan** — A final structured plan is generated.

---

# 🤖 Five AI Analysis Dimensions

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/aa834180-6f0c-48a3-a84d-c7ce9a3ec8fb"
    alt="Five AI Analysis Dimensions"
    width="100%"
  />
</p>

| # | AI Specialist | Main Focus |
|---|---|---|
| 🟢 01 | **Market Research** | Market size, demand, trends and target audience |
| 🟠 02 | **Competitor Analysis** | Competitors, gaps, SWOT and differentiation |
| 🟣 03 | **Financial Planning** | Costs, revenue, expenses and break-even |
| 🔴 04 | **Risk Analysis** | Business risks, impact and mitigation |
| 🔵 05 | **Marketing Strategy** | Positioning, channels, launch and growth |

---

# 📊 What the AI Generates

The final business plan can contain:

### 📌 Executive Summary
Business concept, opportunity and overall direction.

### 📈 Market Opportunity
Target customers, demand, trends and market potential.

### ⚔️ Competitive Landscape
Competitor identification, strengths, gaps and differentiation.

### 💰 Financial Planning
Startup costs, operating expenses, revenue assumptions and break-even considerations.

### ⚠️ Risk Assessment
Financial, market, operational and compliance risks with mitigation strategies.

### 📣 Marketing Strategy
Positioning, marketing channels, launch activities and growth strategy.

### ✅ Recommended Next Steps
Practical actions to move the business idea forward.

---

# 🧠 RAG Architecture

```text
Business Knowledge
        ↓
Document Loading
        ↓
Text Chunking
        ↓
Mistral Embeddings
        ↓
FAISS Vector Store
        ↓
Semantic Retrieval
        ↓
Relevant Context
        ↓
AI Agents
```

The RAG layer provides relevant knowledge to the specialist agents before they generate their analysis.

---

# 🔄 Multi-Agent Workflow

```text
                    BUSINESS IDEA
                         │
                         ▼
                  RAG KNOWLEDGE BASE
                         │
                         ▼
              ┌───────────────────────┐
              │  FIVE AI SPECIALISTS  │
              └───────────────────────┘
                 │    │    │    │    │
                 ▼    ▼    ▼    ▼    ▼
              Market Competitor Finance Risk Marketing
                 │    │    │    │    │
                 └────┴────┴────┴────┘
                         │
                         ▼
                 LANGGRAPH ORCHESTRATOR
                         │
                         ▼
                     SYNTHESIZER
                         │
                         ▼
               COMPLETE BUSINESS PLAN
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core application |
| 🎨 Streamlit | Interactive web interface |
| 🧠 Mistral AI | LLM generation and embeddings |
| 🔗 LangChain | AI/agent components |
| 🔄 LangGraph | Workflow orchestration |
| 📚 RAG | Knowledge-grounded generation |
| ⚡ FAISS | Vector similarity search |

---

# 📁 Project Structure

```text
Autonomous-Buisness-Analyst/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── architecture.svg
├── analysis-dimensions.svg
│
├── agents/
│   ├── base_agent.py
│   ├── market_research.py
│   ├── competitor_analysis.py
│   ├── financial_planner.py
│   ├── risk_analysis.py
│   ├── marketing_strategy.py
│   └── synthesizer.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
├── rag/
│   ├── loader.py
│   └── retriever.py
│
├── utils/
│   └── llm.py
│
├── data/
│   └── business_knowledge.txt
│
└── outputs/
```

---

# 🚀 Run Locally

### 1. Clone

```bash
git clone https://github.com/jatinkumar4148/Autonomous-Buisness-Analyst.git
cd Autonomous-Buisness-Analyst
```

### 2. Create virtual environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API key

Create `.env`:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### 5. Run

```bash
streamlit run main.py
```

Then open:

```text
http://localhost:8501
```

---

# 💡 Example Ideas

```text
I want to open a coffee shop in Delhi.
```

```text
I want to start an online clothing business in Mumbai.
```

```text
I want to launch a fitness subscription app for college students.
```

For better results, provide details such as:

- Location
- Target audience
- Business model
- Approximate budget
- Product/service
- Competitive advantage

---

# 🔐 Environment Variables

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

⚠️ **Never commit your `.env` file or expose your API key publicly.**

---

# 🔧 Customization

You can customize the project by:

- Adding new AI agents
- Updating the RAG knowledge base
- Modifying agent prompts
- Changing the LangGraph workflow
- Adding new business-analysis dimensions
- Improving financial calculations
- Adding additional export formats

---

# 📈 Future Enhancements

- 🌐 Real-time web market research
- 📊 Live competitor pricing
- 💹 Advanced financial forecasting
- 📄 PDF/DOCX report export
- 🧪 Automated testing
- 🗃️ Industry-specific RAG
- ➕ Additional specialist agents
- ☁️ Production monitoring

---

# ⚠️ Disclaimer

This application provides AI-assisted business analysis for planning and educational purposes. Generated information may be incomplete, inaccurate, or outdated. Financial, legal, tax, regulatory [...]

---

<p align="center">

### 🤖 Built with Mistral AI + LangChain + LangGraph + RAG + FAISS

<br>

<a href="https://autonomous-buisness-analyst.streamlit.app/">
  🚀 <strong>Try the Live App</strong>
</a>

</p>
