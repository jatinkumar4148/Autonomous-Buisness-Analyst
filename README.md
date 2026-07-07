# 🤖 Autonomous Business Analyst AI

Transform any business idea into a **complete professional business plan** using 5 AI agents powered by **Mistral AI**, **LangChain**, **LangGraph**, and **RAG (Retrieval Augmented Generation)**.

---

## 🎯 What Does This Project Do?

**Input:** You type your business idea
```
"I want to open a coffee shop in Delhi"
```

**Output:** You get a complete business plan in 5-10 minutes including:
- 📊 **Market Research** — Market size, target customers, trends, demand analysis
- ⚔️ **Competitor Analysis** — Who are competitors, what are their gaps, your differentiation strategy
- 💰 **Financial Plan** — Startup costs, monthly expenses, revenue projections, break-even analysis
- ⚠️ **Risk Analysis** — What can go wrong, mitigation strategies, compliance requirements
- 📣 **Marketing Strategy** — How to reach customers, 90-day launch plan, growth strategy
- 📄 **Executive Summary** — Professional synthesized business plan ready to present

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                   USER INPUT                            │
│          "I want to open a coffee shop"                 │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │    RAG KNOWLEDGE BASE         │
        │  (FAISS Vector Store)         │
        │  - Business insights          │
        │  - Market data                │
        │  - Best practices             │
        └──────────────┬────────────────┘
                       │
         ┌─────────────▼─────────────┐
         │   LANGCHAIN LLM AGENTS    │
         │┌──────────────────────────┐│
         ││ Market Research Agent    ││
         ││ Competitor Analysis Agt  ││
         ││ Financial Planner Agent  ││
         ││ Risk Analysis Agent      ││
         ││ Marketing Strategy Agent ││
         │└──────────────────────────┘│
         └──────────────┬──────────────┘
                        │
         ┌──────────────▼──────────────┐
         │   LANGGRAPH ORCHESTRATOR    │
         │  (Manages agent workflow)   │
         └──────────────┬──────────────┘
                        │
                        ▼
         ┌──────────────────────────────┐
         │   SYNTHESIZER AGENT          │
         │  (Creates final output)      │
         └──────────────┬───────────────┘
                        │
                        ▼
        ┌────────────────────────────────┐
        │  COMPLETE BUSINESS PLAN        │
        │  (Saved as .txt file)          │
        └────────────────────────────────┘
```

---

## 🧬 Tech Stack

| Component | Technology | Role |
|-----------|-----------|------|
| **LLM** | Mistral AI API | Core AI reasoning engine |
| **Framework** | LangChain | Prompt management, chains, memory |
| **Orchestration** | LangGraph | Multi-agent workflow coordination |
| **RAG** | FAISS Vector Store | Semantic search over knowledge base |
| **Embeddings** | Mistral Embeddings | Text vectorization for RAG |
| **Language** | Python 3.9+ | Full project implementation |

---

## 📁 Project Structure

```
autonomous_business_analyst/
│
├── main.py                          ← RUN THIS FILE (entry point)
├── requirements.txt                 ← All dependencies listed
├── .env.example                     ← Copy to .env and add API key
├── .gitignore                       ← Files to ignore in git
├── README.md                        ← This file
│
├── data/
│   └── business_knowledge.txt       ← RAG knowledge base (business insights)
│
├── rag/
│   ├── __init__.py
│   ├── loader.py                    ← Load documents, split into chunks
│   └── retriever.py                 ← FAISS vector store, semantic search
│
├── utils/
│   ├── __init__.py
│   └── llm.py                       ← Mistral LLM + Embeddings connection
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py                ← Base class all agents inherit from
│   ├── market_research.py           ← Agent 1: Market Research
│   ├── competitor_analysis.py       ← Agent 2: Competitor Analysis
│   ├── financial_planner.py         ← Agent 3: Financial Planning
│   ├── risk_analysis.py             ← Agent 4: Risk Analysis
│   ├── marketing_strategy.py        ← Agent 5: Marketing Strategy
│   └── synthesizer.py               ← Final: Synthesize all outputs
│
└── graph/
    ├── __init__.py
    ├── state.py                     ← LangGraph state definition (shared data)
    ├── nodes.py                     ← LangGraph nodes (agent runners)
    └── workflow.py                  ← LangGraph workflow (orchestration)
```

---

## 🚀 Quick Start (4 Steps)

### Step 1: Install Python (if not already installed)
Go to https://www.python.org/downloads/ and install Python 3.9 or higher.

### Step 2: Extract and Setup
```bash
# Extract the ZIP file
cd autonomous_business_analyst

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Step 3: Get Your Mistral API Key
1. Go to https://console.mistral.ai
2. Sign up (free account)
3. Go to API Keys section
4. Create a new API key
5. Copy the key (looks like: `sk-XXXXXXXXXXXXXX`)

### Step 4: Create .env File and Run
```bash
# Create .env file in the project root folder
cat > .env << EOF
MISTRAL_API_KEY=your_api_key_here
EOF

# Windows users can instead create a .env file manually in the project root and paste:
# MISTRAL_API_KEY=your_key_here

# Run the project!
python main.py
```

Then type your business idea and get your complete business plan! 🎉

---

## 📋 How to Use

1. **Run the program**
   ```bash
   python main.py
   ```

2. **Type your business idea when prompted**
   ```
   Examples:
   - "I want to open a coffee shop in Delhi"
   - "I want to start an online clothing store"
   - "I want to launch a fitness app"
   - "I want to open a bakery in Mumbai"
   ```

3. **Wait for analysis** (usually 5-10 minutes)
   The program will:
   - Search the knowledge base for relevant information
   - Run all 5 agents in parallel
   - Synthesize outputs into a final plan

4. **Get your results**
   - Plan printed to screen
   - Plan saved to `outputs/business_plan_*.txt`

---

## 📊 Sample Output

The final business plan includes:

**EXECUTIVE SUMMARY**
- Overview of the business idea
- Market opportunity size
- Why this business can succeed

**MARKET OPPORTUNITY**
- Market size and growth rate
- Target customer profile
- Current market trends
- Demand validation

**COMPETITIVE LANDSCAPE**
- Direct and indirect competitors
- Competitive advantages
- Differentiation strategy
- How to beat competitors

**FINANCIAL PROJECTIONS**
- Startup costs breakdown
- Monthly operating expenses
- Revenue projections (3 months, 6 months, 1 year, 2 years)
- Break-even analysis
- Profitability forecast with scenarios

**RISK MANAGEMENT**
- Risk register with likelihood and impact
- Financial, market, operational risks
- Mitigation strategies for each risk
- Compliance and legal requirements

**GO-TO-MARKET STRATEGY**
- Brand positioning and UVP
- Target audience profile
- Marketing channels and priorities
- Content strategy
- 90-day launch roadmap
- Customer retention strategy

**RECOMMENDED NEXT STEPS**
- 5 immediate actions to get started
- Timeline and priorities
- Resource requirements

---

## 🔌 System Architecture Deep Dive

### Module 1: RAG Pipeline (Knowledge Base Search)
```
Knowledge Base File (business_knowledge.txt)
           ↓
    Text Chunking (800 chars, 100 char overlap)
           ↓
    Mistral Embeddings (vectorization)
           ↓
    FAISS Index (vector database)
           ↓
When Agent Asks: "Market analysis for coffee shop"
           ↓
    Semantic Search (find similar chunks)
           ↓
    Return Top-4 Most Relevant Chunks
```

### Module 2: LangChain Agents
Each agent has:
- **Role**: Clear description (e.g., "Market Research Analyst")
- **System Prompt**: Detailed instructions for the AI
- **RAG Context**: Retrieved from knowledge base
- **LLM Chain**: Prompt → Mistral API → Response Parser

### Module 3: LangGraph Workflow
```
START
  ↓
market_research_node (Agent 1)
  ↓
competitor_analysis_node (Agent 2)
  ↓
financial_planner_node (Agent 3)
  ↓
risk_analysis_node (Agent 4)
  ↓
marketing_strategy_node (Agent 5)
  ↓
synthesizer_node (Final synthesis)
  ↓
OUTPUT
```

All agent outputs are stored in shared state and passed to synthesizer.

---

## 🔑 Environment Variables

Create a `.env` file with:
```
MISTRAL_API_KEY=your_mistral_api_key_here
```

**Never commit .env to GitHub!** It's already in .gitignore.

---

## ⚙️ Customization Guide

### Add More Agents
1. Create `agents/my_agent.py`
2. Inherit from `BaseAgent`
3. Define `MY_AGENT_PROMPT`
4. Add to `graph/nodes.py`
5. Add edge to workflow in `graph/workflow.py`

### Update Knowledge Base
Edit `data/business_knowledge.txt` with your knowledge. The RAG system will automatically:
- Split into chunks
- Create embeddings
- Make searchable

### Adjust Agent Behavior
Edit the system prompts in each agent file to change:
- Tone (formal vs casual)
- Detail level (brief vs comprehensive)
- Focus areas (what to emphasize)

### Modify Workflow Order
Edit `graph/workflow.py` to change agent sequence or skip agents.

---

## 🐛 Troubleshooting

### Error: "MISTRAL_API_KEY not found"
**Fix:** Create `.env` file and add your API key (see Quick Start Step 3)

### Error: "No module named 'langchain'"
**Fix:** Run `pip install -r requirements.txt`

### Slow responses
- First run is slower (FAISS index building)
- Mistral API response time depends on payload size
- Check internet connection

### Low quality outputs
- Customize system prompts in agent files
- Add more/better content to knowledge base
- Use more specific business idea input

---

## 📈 Costs

### Mistral API Pricing
- **Free Trial**: Free credits when you sign up (~$5 worth)
- **Pay As You Go**: 
  - Input: ~$0.14 per 1M tokens
  - Output: ~$0.42 per 1M tokens
  - Average business plan: ~20,000 tokens = ~$0.01

**Total cost per business plan: ₹0.50 - ₹2 (very cheap!)**

### Cloud Infrastructure
Everything runs **locally on your computer**. No cloud costs.

---

## 📚 Learning Resources

- **Mistral Docs**: https://docs.mistral.ai
- **LangChain Docs**: https://python.langchain.com
- **LangGraph Docs**: https://langchain-ai.github.io/langgraph/
- **FAISS**: https://github.com/facebookresearch/faiss
- **RAG Concepts**: https://en.wikipedia.org/wiki/Retrieval-augmented_generation

---

## 🤝 Contributing

Found a bug or want to improve it? 
- Add better prompts in agent files
- Expand knowledge base
- Optimize RAG retrieval
- Add new agents for specific industries

---

## 📄 License

This project is provided as-is for learning and commercial use.

---

## ❓ FAQ

**Q: Can I use this commercially?**
A: Yes! You'll need a Mistral API key (paid plan if scaling), but no restrictions on using outputs.

**Q: Can I modify it for my industry?**
A: Absolutely! Update prompts and knowledge base for your specific industry.

**Q: What if I want to use a different LLM (GPT-4, Claude, etc.)?**
A: Modify `utils/llm.py` to use different provider's API.

**Q: Is this better than ChatGPT?**
A: Different use case! This is specialized for business plans. ChatGPT is general-purpose. This is more accurate for business analysis due to RAG + specialized agents.

**Q: How is data privacy handled?**
A: Your business idea is sent to Mistral API for processing. Knowledge base stays local. No data stored permanently. Check Mistral's privacy policy.

---

## 🎓 What You'll Learn

By studying this project, you'll understand:
- ✅ How to build LLM applications with LangChain
- ✅ Multi-agent coordination with LangGraph
- ✅ RAG systems with FAISS
- ✅ Prompt engineering and system prompts
- ✅ LLM orchestration patterns
- ✅ Production-ready Python project structure

---

## 🚀 Ready to Get Started?

1. **Get your API key**: https://console.mistral.ai
2. **Run the setup** (see Quick Start)
3. **Type your business idea**
4. **Get your complete business plan in minutes!**

**Questions?** Review the code comments — everything is well-documented.

Enjoy building! 🎉

├── agents/
│   ├── base_agent.py          ← Base class all agents inherit
│   ├── market_research.py     ← Agent 1
│   ├── competitor_analysis.py ← Agent 2
│   ├── financial_planner.py   ← Agent 3
│   ├── risk_analysis.py       ← Agent 4
│   ├── marketing_strategy.py  ← Agent 5
│   └── synthesizer.py         ← Final report generator
│
├── graph/
│   ├── state.py               ← LangGraph shared state
│   ├── nodes.py               ← Each agent as a graph node
│   └── workflow.py            ← Pipeline builder
│
└── outputs/                   ← Generated business plans saved here
```

---

## ⚙️ Setup & Installation (Step by Step)

### Step 1 — Make sure Python is installed
```bash
python --version
# Should show Python 3.9 or higher
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Get your Mistral API Key (FREE)
1. Go to: https://console.mistral.ai
2. Sign up for a free account
3. Click "API Keys" → "Create new key"
4. Copy the key (starts with something like: xxxxxxxx...)

### Step 4 — Create your .env file
Create a file named `.env` in the project root and add:
```
MISTRAL_API_KEY=your_actual_key_here
```

### Step 5 — Run the project!
```bash
python main.py
```

---

## 🚀 Example Run

```
$ python main.py

=================================================================
  🤖  AUTONOMOUS BUSINESS ANALYST AI
  Powered by: Mistral + LangChain + LangGraph + RAG
=================================================================

👉 Enter your business idea: I want to open a coffee shop in Delhi

📂 Loading documents from: data/
✅ Loaded 1 document(s)
✅ Split into 32 chunks
🧠 Creating embeddings with Mistral...
✅ Vector store ready!

🤖 Running: Market Research Agent...
✅ Market Research Agent completed!

🤖 Running: Competitor Analysis Agent...
✅ Competitor Analysis Agent completed!

... (all 5 agents run) ...

📝 Synthesizer: Creating final business plan...
✅ Final business plan ready!

✅ Business plan saved to: outputs/business_plan_coffee_shop_delhi.txt
⏱️  Total time: 45.2 seconds
```

---

## 💡 Tips

- Add your own documents to the `data/` folder to expand the knowledge base
- Supported document formats: `.txt` files (add PDF support via PyPDFLoader)
- Each run saves a timestamped `.txt` file in the `outputs/` folder
- The free Mistral tier is enough for testing this project

---

## 🔑 Important: Keep Your API Key Safe

- Never share your `.env` file
- Never push `.env` to GitHub (it's in `.gitignore`)
- If your key is leaked, go to https://console.mistral.ai and regenerate it

---

## 📜 License

MIT License — Free to use, modify, and share.
