🤖 Autonomous Business Analyst AI

<p align="center">
  <strong>Turn one business idea into a structured, professional business plan using a multi-agent AI workflow.</strong>
</p>

<p align="center">
  <a href="https://autonomous-buisness-analyst.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Streamlit-FF4B4B?style=for-the-badge" alt="Live Demo">
  </a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Mistral%20AI-LLM-111827?style=for-the-badge" alt="Mistral AI">
  <img src="https://img.shields.io/badge/LangGraph-Workflow-16A34A?style=for-the-badge" alt="LangGraph">
  <img src="https://img.shields.io/badge/RAG-FAISS-F59E0B?style=for-the-badge" alt="RAG FAISS">
</p>

<p align="center">
  <a href="https://github.com/jatinkumar4148/Autonomous-Buisness-Analyst">📦 GitHub Repository</a>
  &nbsp; • &nbsp;
  <a href="https://autonomous-buisness-analyst.streamlit.app/">🌐 Live Application</a>
</p>

🌐 Live Demo

🚀 Try it yourself

Open Autonomous Business Analyst AI →

Enter a business idea such as:

“I want to open a specialty coffee shop in Delhi for students and remote workers.”

The application analyzes the idea across five specialist dimensions and generates a complete business plan.

⚠️ Important: This tool produces AI-assisted estimates and recommendations. Validate market data, legal requirements, pricing, and financial projections with qualified local professionals before making business decisions.

✨ What is this?

Autonomous Business Analyst AI is a Streamlit-based multi-agent business analysis application that turns a business idea into a structured business plan using:

🧠 Mistral AI for language generation and embeddings

🔗 LangChain for LLM/agent components

🔄 LangGraph for workflow orchestration

📚 RAG + FAISS for knowledge-grounded responses

📊 Five specialist AI agents for business analysis

The five core areas are Market Research, Competitor Analysis, Financial Planning, Risk Analysis, and Marketing Strategy, followed by a final synthesis into one business plan.

🧩 System Architecture

<p align="center">
  <img src="<img width="1672" height="940" alt="bb1ccf65-fe0e-4f22-a383-f4369adbcbd1" src="https://github.com/user-attachments/assets/0397de42-ded7-4897-8cda-2130e6e4e898" />
" alt="Autonomous Business Analyst AI system architecture" width="100%">
</p>

🔄 End-to-end flow

Business Idea → RAG Knowledge Base → Five AI Agents → LangGraph Orchestrator → Synthesizer → Complete Business Plan

The workflow stores each specialist result in shared LangGraph state and then combines those results into the final report.

🤖 Five Specialized AI Agents

<p align="center">
  <img src="<img width="1690" height="931" alt="d4939f05-73ae-44d3-94a3-76f13550f927" src="https://github.com/user-attachments/assets/f1789c97-5338-4abd-b0d7-aa36d5100c5d" />" alt="Five AI analysis dimensions" width="100%">
</p>

#

Specialist Agent

Focus

01

📊 Market Research

Target customers, demand, trends, market opportunity and entry timing

02

⚔️ Competitor Analysis

Direct/indirect competitors, SWOT-style insights, pricing and differentiation

03

💰 Financial Planning

Startup costs, operating expenses, revenue scenarios and break-even

04

🛡️ Risk Analysis

Financial, market, operational, regulatory and legal risks

05

📣 Marketing Strategy

Positioning, channels, launch activities, acquisition and retention

🎯 Final Synthesis

The Synthesizer combines the outputs from all five specialists into one coherent business plan.

📋 What you get

The dashboard can produce sections such as:

📌 Executive summary

🏢 Business overview

📈 Market opportunity

⚔️ Competitive landscape

💰 Financial projections

⚠️ Risk management

🚀 Go-to-market strategy

✅ Recommended next steps

Generated reports are also saved locally in:

outputs/business_plan_<business_idea>_<timestamp>.txt

🧠 RAG Pipeline

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
Specialist AI Agents

The local knowledge base is stored in:

data/business_knowledge.txt

Relevant retrieved context is added to agent prompts to make responses more knowledge-grounded.

🔄 Multi-Agent Workflow

START
  ↓
Market Research
  ↓
Competitor Analysis
  ↓
Financial Planning
  ↓
Risk Analysis
  ↓
Marketing Strategy
  ↓
Synthesizer
  ↓
FINAL BUSINESS PLAN

LangGraph coordinates the workflow and shared state between the specialist agents.

🛠️ Technology Stack

Area

Technology

🎨 User Interface

Streamlit

🧠 Language Model

Mistral AI

🔗 LLM / Agent Framework

LangChain

🔄 Workflow Orchestration

LangGraph

📚 Retrieval

RAG + FAISS

🧮 Embeddings

Mistral Embeddings

🐍 Language

Python 3.9+

📁 Project Structure

autonomous_business_analyst/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── data/
│   └── business_knowledge.txt
│
├── rag/
│   ├── __init__.py
│   ├── loader.py
│   └── retriever.py
│
├── utils/
│   ├── __init__.py
│   └── llm.py
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── market_research.py
│   ├── competitor_analysis.py
│   ├── financial_planner.py
│   ├── risk_analysis.py
│   ├── marketing_strategy.py
│   └── synthesizer.py
│
├── graph/
│   ├── __init__.py
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
└── outputs/

🚀 Run Locally

1. Clone the repository

git clone https://github.com/jatinkumar4148/Autonomous-Buisness-Analyst.git
cd Autonomous-Buisness-Analyst

2. Create a virtual environment

Windows PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1

Windows CMD

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure Mistral API

Create a .env file in the project root:

MISTRAL_API_KEY=your_mistral_api_key_here

You can use .env.example as the template.

Never commit .env or expose your API key in GitHub.

5. Run Streamlit

streamlit run main.py

Then open:

http://localhost:8501

💡 Good Input Examples

I want to open a specialty coffee shop in Delhi for students and remote workers.

I want to start an affordable online clothing store for urban Indian customers.

I want to launch a subscription-based fitness app for beginners in Mumbai.

For better results, include the location, target customer, business model, budget, and differentiator when known.

🔐 Security & Privacy

Keep API keys inside .env.

Do not hard-code API keys.

Do not commit .env.

Do not upload confidential business plans or customer data.

Business ideas and prompts are sent to Mistral for processing.

Review provider privacy policies before using sensitive information.

🧪 Development Checks

Compile-check the project:

python -m compileall main.py agents graph rag utils

Run the application:

streamlit run main.py

🐛 Troubleshooting

MISTRAL_API_KEY is missing

Check that .env exists beside main.py and contains:

MISTRAL_API_KEY=your_mistral_api_key_here

Restart Streamlit after changing environment variables.

ModuleNotFoundError

python -m pip install -r requirements.txt

FAISS / embedding errors

Check that dependencies installed correctly and that the machine has internet access for the initial embedding request.

Analysis is slow

The first run may build the vector store. Each analysis also makes multiple model calls and a final synthesis call.

Results are too generic

Use a more specific business idea, improve the local knowledge base, and refine the relevant specialist prompt.

🔧 Customization

Update the knowledge base

Edit:

data/business_knowledge.txt

Change agent behavior

Edit the specialist prompts and role definitions under:

agents/

Change workflow

Update:

graph/nodes.py
graph/workflow.py

Change model configuration

Update:

utils/llm.py

📈 Future Improvements

Potential extensions include:

🌐 Web-based market research

📊 Real-time competitor pricing

💹 More detailed financial modeling

📄 PDF / DOCX export

🧪 Automated tests

➕ Additional specialist agents

🗃️ Industry-specific RAG knowledge bases

☁️ Production deployment and monitoring

📜 License

No license file is currently included in the repository. Add an explicit license before distributing the project or accepting external contributions.

⚠️ Disclaimer

This project is for research, planning, and educational use. AI-generated content can be incomplete, inaccurate, or outdated. It is not financial, legal, tax, investment, or professional business advice.

<p align="center">
  <strong>Built with 🤖 Mistral AI • 🔗 LangChain • 🔄 LangGraph • 📚 RAG + FAISS</strong>
</p>

<p align="center">
  <a href="https://autonomous-buisness-analyst.streamlit.app/">🚀 Live Demo</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/jatinkumar4148/Autonomous-Buisness-Analyst">⭐ GitHub</a>
</p>
