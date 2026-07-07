# 🏗️ Project Structure & Architecture

Complete technical documentation of the Autonomous Business Analyst AI project.

---

## 📁 Folder Layout

```
autonomous_business_analyst/
│
├─ 📄 main.py                      ← ENTRY POINT (run this)
├─ 📄 README.md                    ← Project overview
├─ 📄 SETUP_GUIDE.md               ← Installation instructions
├─ 📄 PROJECT_STRUCTURE.md         ← This file
├─ 📄 requirements.txt             ← Package dependencies
├─ 📄 .env.example                 ← Environment template
├─ 📄 .gitignore                   ← Git ignore rules
│
├─ 📁 data/
│  └─ 📄 business_knowledge.txt    ← RAG knowledge base
│
├─ 📁 rag/
│  ├─ 📄 __init__.py               ← Package init
│  ├─ 📄 loader.py                 ← Document loader & chunker
│  └─ 📄 retriever.py              ← FAISS vector store & search
│
├─ 📁 utils/
│  ├─ 📄 __init__.py               ← Package init
│  └─ 📄 llm.py                    ← Mistral API connector
│
├─ 📁 agents/
│  ├─ 📄 __init__.py               ← Package init
│  ├─ 📄 base_agent.py             ← Base class for all agents
│  ├─ 📄 market_research.py        ← Agent 1: Market Research
│  ├─ 📄 competitor_analysis.py    ← Agent 2: Competitor Analysis
│  ├─ 📄 financial_planner.py      ← Agent 3: Financial Planning
│  ├─ 📄 risk_analysis.py          ← Agent 4: Risk Analysis
│  ├─ 📄 marketing_strategy.py     ← Agent 5: Marketing Strategy
│  └─ 📄 synthesizer.py            ← Final synthesis
│
├─ 📁 graph/
│  ├─ 📄 __init__.py               ← Package init
│  ├─ 📄 state.py                  ← LangGraph state definition
│  ├─ 📄 nodes.py                  ← Workflow nodes
│  └─ 📄 workflow.py               ← LangGraph orchestration
│
└─ 📁 outputs/                     ← Generated business plans
   └─ business_plan_*.txt          ← Output files
```

---

## 🔌 Module Details

### Module 1: Entry Point (main.py)

**Purpose:** Single entry point for the entire application.

**Flow:**
```
1. Print welcome banner
2. Check for MISTRAL_API_KEY in .env
3. Get business idea from user input
4. Initialize RAG vector store
5. Run LangGraph workflow with all agents
6. Display results section by section
7. Save complete plan to file
```

**Key Functions:**
- `print_banner()` — Display welcome message
- `print_section(title, content)` — Format output sections
- `save_report(business_idea, report)` — Save to `outputs/` folder
- `run_business_analyst(business_idea)` — Main pipeline
- `main()` — Entry point

**Execution Time:** 5-10 minutes total

---

### Module 2: Utilities (utils/llm.py)

**Purpose:** Connection to Mistral AI API and embeddings.

**Exports:**
- `get_llm(temperature=0.3)` — Returns ChatMistralAI instance
- `get_embeddings()` — Returns MistralAIEmbeddings instance

**LLM Configuration:**
- Model: `mistral-medium-latest`
- Temperature: 0.3 (focused, not creative)
- Token limit: ~8000 tokens per request

**Embeddings Configuration:**
- Model: `mistral-embed`
- Dimension: 1024
- Used for FAISS vector store

**Error Handling:**
```python
if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY not found in .env file!")
```

---

### Module 3: RAG Pipeline (rag/)

#### 3.1 Document Loader (rag/loader.py)

**Purpose:** Load business knowledge and split into chunks.

**Functions:**
- `load_documents(data_dir)` — Load all .txt files from folder
- `split_documents(documents)` — Split into overlapping chunks
- `load_and_split(data_dir)` — Convenience function

**Chunking Strategy:**
```python
chunk_size=800          # Each chunk ~800 characters
chunk_overlap=100       # 100 char overlap between chunks
separators=["\n\n", "\n", ".", " "]  # Split order
```

**Why Chunking?**
- Too large chunks: AI gets lost in content
- Too small chunks: Lose important context
- Overlap: Ensures important info at boundaries isn't lost

#### 3.2 Vector Store (rag/retriever.py)

**Purpose:** Create searchable index and retrieve relevant context.

**Architecture:**
```
Knowledge Base (business_knowledge.txt)
    ↓
Text Splitting (800 chars, 100 overlap)
    ↓
Mistral Embeddings (convert to vectors)
    ↓
FAISS Index (search-optimized storage)
    ↓
Similarity Search (find top-k similar chunks)
```

**Functions:**
- `build_vector_store(data_dir)` — Create FAISS index from documents
- `get_vector_store(data_dir)` — Get cached store (builds if needed)
- `retrieve_context(query, k=4)` — Search and return top chunks

**Caching:**
```python
_vector_store: Optional[FAISS] = None  # Cached in memory
```

The vector store is built once per session, then reused.

**Retrieval Example:**
```python
query = "Market research for coffee shop in India"
context = retrieve_context(query, k=4)  # Top 4 chunks
# Returns formatted string:
# "[Context 1]:\n..."
# "[Context 2]:\n..."
```

---

### Module 4: Agents (agents/)

#### 4.1 Base Agent Class (agents/base_agent.py)

**Purpose:** Template that all 5 agents inherit from.

**Class: BaseAgent**
```python
class BaseAgent:
    def __init__(self, role: str, system_prompt: str):
        self.role = role                          # e.g., "Market Research Agent"
        self.system_prompt = system_prompt        # Detailed instructions
        self.llm = get_llm(temperature=0.4)      # Mistral API
        self.output_parser = StrOutputParser()    # Parse response

    def run(self, business_idea: str) -> str:
        # 1. Retrieve context from RAG
        # 2. Build prompt with context
        # 3. Call Mistral LLM
        # 4. Parse and return response
```

**Chain Pipeline:**
```
Prompt Template
    ↓
Mistral LLM (via LangChain)
    ↓
Output Parser
```

#### 4.2 Agent 1: Market Research (agents/market_research.py)

**Prompt Focus:**
- Market size and growth rate
- Target customer profile
- Market trends
- Demand validation
- Market entry timing

**Role:** Expert Market Research Analyst with 15 years experience

#### 4.3 Agent 2: Competitor Analysis (agents/competitor_analysis.py)

**Prompt Focus:**
- Direct and indirect competitors
- SWOT analysis for each
- Competitive gaps
- Differentiation strategy
- Pricing benchmark

**Role:** Business Strategy Analyst specializing in competitive intelligence

#### 4.4 Agent 3: Financial Planner (agents/financial_planner.py)

**Prompt Focus:**
- Startup costs (infrastructure, equipment, inventory)
- Monthly operating expenses (fixed vs variable)
- Revenue projections (3mo, 6mo, 1yr, 2yr)
- Break-even analysis
- Profitability forecast with scenarios

**Role:** Senior Financial Advisor and startup finance expert

#### 4.5 Agent 4: Risk Analyst (agents/risk_analysis.py)

**Prompt Focus:**
- Risk register (description, likelihood, impact, score)
- Financial, market, operational risks
- Regulatory and legal risks
- Mitigation strategies for each
- Emergency/exit plans

**Role:** Risk Management Consultant and Business Advisor

#### 4.6 Agent 5: Marketing Strategy (agents/marketing_strategy.py)

**Prompt Focus:**
- Brand positioning and UVP
- Target audience profile
- Marketing channels and priorities
- Content strategy
- 90-day launch roadmap
- Customer retention
- Budget allocation
- KPIs to track

**Role:** Digital Marketing Strategist and Brand Expert

#### 4.7 Synthesizer (agents/synthesizer.py)

**Purpose:** Take all 5 agent outputs and create final professional report.

**Function: synthesize_business_plan()**
- Takes 6 inputs: business_idea + 5 agent outputs
- Creates single ChatPromptTemplate
- Calls Mistral LLM with all context
- Returns formatted business plan

**Output Format:**
```
1. Executive Summary (2-3 paragraphs)
2. Business Overview
3. Market Opportunity
4. Competitive Landscape
5. Financial Projections
6. Risk Management
7. Go-to-Market Strategy
8. Conclusion & Next Steps (5 action items)
```

---

### Module 5: LangGraph Orchestration (graph/)

#### 5.1 State Definition (graph/state.py)

**Purpose:** Define shared data passed between all agents.

**Class: BusinessAnalystState (TypedDict)**
```python
class BusinessAnalystState(TypedDict):
    # Input
    business_idea: str
    
    # Agent outputs (filled one by one)
    market_research: Optional[str]
    competitor_analysis: Optional[str]
    financial_plan: Optional[str]
    risk_analysis: Optional[str]
    marketing_strategy: Optional[str]
    
    # Final output
    final_report: Optional[str]
    
    # Status tracking
    current_step: Optional[str]
    error: Optional[str]
```

**Why TypedDict?**
- Type-safe state management
- IDE autocomplete support
- Clear contract for data flow

#### 5.2 Workflow Nodes (graph/nodes.py)

**Purpose:** Define what each node does.

**6 Node Functions:**

1. `market_research_node(state)` → Runs market research agent
2. `competitor_analysis_node(state)` → Runs competitor analysis agent
3. `financial_planner_node(state)` → Runs financial planner agent
4. `risk_analysis_node(state)` → Runs risk analysis agent
5. `marketing_strategy_node(state)` → Runs marketing strategy agent
6. `synthesizer_node(state)` → Synthesizes all outputs

**Node Pattern:**
```python
def node_name(state: BusinessAnalystState) -> BusinessAnalystState:
    try:
        result = run_agent(state["business_idea"])
        return {
            **state,                    # Keep existing data
            "field_key": result,       # Add new result
            "current_step": "step_done"
        }
    except Exception as e:
        return {**state, "error": str(e)}
```

#### 5.3 Workflow Orchestration (graph/workflow.py)

**Purpose:** Connect nodes into a workflow pipeline.

**Function: build_workflow()**

**Step 1: Create Graph**
```python
workflow = StateGraph(BusinessAnalystState)
```

**Step 2: Add Nodes**
```python
workflow.add_node("market_research", market_research_node)
workflow.add_node("competitor_analysis", competitor_analysis_node)
# ... etc
```

**Step 3: Define Edges (connections)**
```python
workflow.set_entry_point("market_research")
workflow.add_edge("market_research", "competitor_analysis")
workflow.add_edge("competitor_analysis", "financial_planner")
# ... etc
workflow.add_edge("synthesizer", END)
```

**Execution Flow:**
```
START
  ↓
market_research_node
  ↓ (state updated with market_research)
competitor_analysis_node
  ↓ (state updated with competitor_analysis)
financial_planner_node
  ↓ (state updated with financial_plan)
risk_analysis_node
  ↓ (state updated with risk_analysis)
marketing_strategy_node
  ↓ (state updated with marketing_strategy)
synthesizer_node
  ↓ (state updated with final_report)
END
```

**Step 4: Compile**
```python
app = workflow.compile()
```

---

## 🔄 Data Flow Diagram

```
USER INPUT
"Coffee shop in Delhi"
    ↓
.env file checks MISTRAL_API_KEY
    ↓
RAG System:
├─ Load business_knowledge.txt
├─ Split into 800-char chunks
├─ Create FAISS embeddings
└─ Builds searchable index
    ↓
LangGraph State initialized:
{
    business_idea: "Coffee shop in Delhi",
    market_research: None,
    competitor_analysis: None,
    financial_plan: None,
    risk_analysis: None,
    marketing_strategy: None,
    final_report: None,
    current_step: "starting",
    error: None
}
    ↓
WORKFLOW EXECUTION:
    ↓
Agent 1: market_research_node
├─ Retrieve: retrieve_context("Market Research for coffee shop in Delhi", k=4)
├─ Prompt: Mistral system_prompt + context + business_idea
├─ LLM: Mistral processes prompt
└─ Update state: market_research = result
    ↓
Agent 2: competitor_analysis_node (same pattern)
    ↓
Agent 3: financial_planner_node (same pattern)
    ↓
Agent 4: risk_analysis_node (same pattern)
    ↓
Agent 5: marketing_strategy_node (same pattern)
    ↓
Synthesizer: synthesizer_node
├─ Input: state with all 5 agent outputs
├─ Prompt: "Create professional business plan from these 5 reports"
├─ LLM: Mistral synthesizes
└─ Update state: final_report = result
    ↓
OUTPUT:
├─ Print each section to console
├─ Save complete plan to outputs/business_plan_*.txt
└─ Display success message
```

---

## 📊 Key Files Explained

### requirements.txt
```
langchain>=0.2.0              # LLM framework
langchain-community>=0.2.0    # Loaders, tools
langchain-mistralai>=0.1.0    # Mistral integration
langchain-text-splitters>=0.2.0  # Document chunking
langgraph>=0.1.0              # Workflow orchestration
faiss-cpu>=1.7.4              # Vector search
python-dotenv>=1.0.0          # .env file loading
mistralai>=1.0.0              # Mistral API client
tiktoken>=0.7.0               # Token counting
```

### data/business_knowledge.txt
- **Size:** ~10-15 KB of knowledge
- **Content:** Business insights, market data, best practices
- **Format:** Plain text sections
- **Used By:** RAG system for context retrieval
- **Format:** Text chunks on topics like:
  - Market Research Fundamentals
  - Competitor Analysis
  - Financial Planning
  - Risk Management
  - Marketing Strategy

### .env.example
Template for environment variables. Users copy to `.env` and add their API key.

### .gitignore
Prevents committing:
- `.env` (API keys)
- `__pycache__/` (Python cache)
- `venv/` (Virtual environment)
- `outputs/` (Generated files)
- `.faiss` files (Vector index)

---

## 🔐 Security Considerations

### Mistral API Key
- **Storage:** In `.env` file (never committed)
- **Usage:** Loaded via `python-dotenv`
- **Protection:** Listed in `.gitignore`

### Data Privacy
- Business ideas sent to Mistral API
- Local files not transmitted
- Check Mistral's privacy policy

### Free Tier Limits
- Monitor API usage in console.mistral.ai
- Free credits are limited (~$5)
- Set up billing alerts if using extensively

---

## 📈 Scalability & Customization

### Adding a New Agent
1. Create `agents/new_agent.py`
2. Define `NEW_AGENT_PROMPT`
3. Create class inheriting from `BaseAgent`
4. Create `run_new_agent(business_idea)` function
5. Add to `graph/nodes.py`: `new_agent_node(state)`
6. Add to `graph/workflow.py`: `add_node()` and `add_edge()`

### Modifying Agent Behavior
- Edit system prompts in agent files
- Change temperature (lower = focused, higher = creative)
- Modify RAG retrieval (change k value)

### Changing LLM Provider
1. Modify `utils/llm.py`
2. Replace `ChatMistralAI` with different provider
3. Update requirements.txt
4. Update system prompts if needed

### Expanding Knowledge Base
1. Add more content to `data/business_knowledge.txt`
2. RAG system automatically chunks and indexes it
3. Next run will have access to new knowledge

---

## 🧪 Testing & Debugging

### Test with Simple Input
```bash
python main.py
# Enter: "E-commerce store"
```

### Check API Key
```python
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("MISTRAL_API_KEY"))
```

### Test RAG Retrieval
```python
from rag.retriever import retrieve_context
context = retrieve_context("market trends")
print(context)
```

### Test Individual Agent
```python
from agents.market_research import run_market_research
result = run_market_research("Coffee shop")
print(result)
```

### Check LangGraph State
```python
from graph.state import BusinessAnalystState
state = {
    "business_idea": "Test",
    "market_research": None,
    # ... etc
}
print(state)
```

---

## 📚 Learning Resources

**LangChain:** https://python.langchain.com/docs
**LangGraph:** https://langchain-ai.github.io/langgraph/
**Mistral Docs:** https://docs.mistral.ai
**FAISS:** https://github.com/facebookresearch/faiss
**RAG Concepts:** https://github.com/mistralai/cookbook

---

## 🚀 Performance Tips

1. **First run is slower** — FAISS index building takes time (~1 min)
2. **Subsequent runs are faster** — Index is cached in memory
3. **API calls are slow** — Mistral processingis network-dependent
4. **Large context is slow** — More tokens = slower processing
5. **Better knowledge base** = Better outputs

---

## 🎯 Summary

This project demonstrates:
- ✅ RAG systems (FAISS + embeddings)
- ✅ Multi-agent orchestration (LangGraph)
- ✅ LLM integration (Mistral + LangChain)
- ✅ Task decomposition (5 specialized agents)
- ✅ Production code structure

All ~600 lines of Python code following software engineering best practices!
