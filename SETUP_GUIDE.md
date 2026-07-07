# 📋 Complete Setup Guide — Autonomous Business Analyst AI

This guide walks you through every step needed to run the project on your computer.

---

## ✅ Pre-Setup Checklist

Before you start, ensure you have:
- [ ] A computer with Windows, Mac, or Linux
- [ ] Internet connection (for Mistral API)
- [ ] ~30 minutes of time
- [ ] A text editor (VS Code, Notepad, etc.)
- [ ] Administrator access to install Python (if needed)

---

## 🔧 Step 1: Install Python (If You Don't Have It)

### Check if Python is Already Installed
```bash
python --version
```

If you see version 3.9 or higher, skip to Step 2. Otherwise:

1. Go to https://www.python.org/downloads/
2. Download **Python 3.10 or 3.11** (recommended)
3. Run the installer
4. **IMPORTANT**: Check the box "Add Python to PATH"
5. Click Install
6. Verify: Open Command Prompt and type `python --version`

---

## 🔑 Step 2: Get Your Mistral API Key

### 2.1 Sign Up
1. Go to https://console.mistral.ai
2. Click "Sign Up"
3. Use email or Google account
4. Verify your email

### 2.2 Create API Key
1. log into console.mistral.ai
2. Click your profile → "API Keys"
3. Click "Create new API Key"
4. Give it a name: `my-business-analyst`
5. Click "Create"
6. **Copy the key** (looks like: `sk-xxxxxxxxxxxxxx`)
7. **Save it safely** — you'll use it in Step 4

### 2.3 Check Free Credits
- New accounts get free credits automatically
- Check your account balance to confirm

---

## 📦 Step 3: Extract and Navigate Project

### 3.1 Extract the ZIP
1. Right-click the ZIP file
2. Select "Extract All" (Windows) or "Extract" (Mac)
3. A folder named `autonomous_business_analyst` will be created

### 3.2 Open Terminal in Project Folder

**Windows:**
1. Open the `autonomous_business_analyst` folder
2. Click address bar at top
3. Type `cmd` and press Enter
4. A command window will open in that folder

**Mac/Linux:**
1. Open Terminal
2. Type: `cd /path/to/autonomous_business_analyst`
3. (Get the path by right-clicking the folder)

### 3.3 Verify Project Structure
Type this command to see all files:
```bash
dir                    # Windows
ls -la                 # Mac/Linux
```

You should see:
- `main.py`
- `requirements.txt`
- `.env.example`
- Folders: `agents/`, `rag/`, `graph/`, `data/`, `utils/`

---

## 🚀 Step 4: Create .env File with Your API Key

### 4.1 Create the File

**Windows (using Command Prompt):**
```bash
copy .env.example .env
```

**Mac/Linux:**
```bash
cp .env.example .env
```

### 4.2 Add Your API Key
1. Open the `.env` file in a text editor
2. Find the line: `MISTRAL_API_KEY=your_mistral_api_key_here`
3. Replace `your_mistral_api_key_here` with your actual key from Step 2
4. **Example:**
   ```
   MISTRAL_API_KEY=sk-abc123xyz789abc123xyz789
   ```
5. Save the file
6. **Do NOT share this file** — it contains your API key!

### 4.3 Verify
Type this to check if file exists:
```bash
cat .env                  # Mac/Linux
type .env                 # Windows
```

You should see your API key printed.

---

## 📚 Step 5: Install Python Dependencies

### 5.1 Install All Required Packages
```bash
pip install -r requirements.txt
```

This will take 2-5 minutes. You'll see several lines of output.

### 5.2 Verify Installation
```bash
pip list
```

You should see:
- `langchain`
- `langgraph`
- `langchain-mistralai`
- `faiss-cpu`
- `python-dotenv`
- `mistralai`

---

## ✨ Step 6: Run the Project!

### 6.1 Start the Program
```bash
python main.py
```

### 6.2 You'll See This Output
```
═════════════════════════════════════════════════════════
  🤖  AUTONOMOUS BUSINESS ANALYST AI
  Powered by: Mistral + LangChain + LangGraph + RAG
═════════════════════════════════════════════════════════

What business do you want to start?
Examples:
  • I want to open a coffee shop in Delhi
  • I want to start an online clothing store
  • I want to launch a fitness app
  • I want to open a bakery in Mumbai

👉 Enter your business idea: _
```

### 6.3 Type Your Business Idea
```
👉 Enter your business idea: I want to open a coffee shop in Delhi
```

### 6.4 Wait for Results (5-10 minutes)
The program will:
1. Build the RAG knowledge base (1-2 min)
2. Run all 5 agents (3-5 min)
3. Synthesize the final report (1-2 min)

You'll see progress like:
```
Module 1/3 — Building RAG Knowledge Base
🔧 Building RAG vector store...
🧠 Creating embeddings with Mistral...
✅ Vector store ready!

Module 2/3 — Running 5 AI Agents via LangGraph
🤖 Running: Market Research Agent...
✅ Market Research Agent completed!
...
```

### 6.5 Get Your Results

The program will:
1. **Print to screen**: All sections of the business plan
2. **Save to file**: `outputs/business_plan_[name]_[date]_[time].txt`

---

## 📊 What You Get

A complete business plan document with:

```
═══════════════════════════════════════════════════════
  🏆  FINAL BUSINESS PLAN (SYNTHESIZED)
═══════════════════════════════════════════════════════

EXECUTIVE SUMMARY
[Concise 2-3 paragraph overview]

BUSINESS OVERVIEW
[Details about your business]

MARKET OPPORTUNITY
[Market size, trends, demand]

COMPETITIVE LANDSCAPE
[Competitors analysis, your advantages]

FINANCIAL PROJECTIONS
[Startup costs, revenue projections, break-even]

RISK MANAGEMENT
[Risks and mitigation strategies]

GO-TO-MARKET STRATEGY
[Marketing plan, channels, launch roadmap]

CONCLUSION & NEXT STEPS
[5 immediate action items]
```

---

## 🐛 Troubleshooting

### Problem: "MISTRAL_API_KEY not found"
**Solution:**
1. Check if `.env` file exists (not `.env.example`)
2. Open `.env` and verify your API key is there
3. Make sure there's no space before `MISTRAL_API_KEY=`

### Problem: "No module named 'langchain'"
**Solution:**
1. Run: `pip install -r requirements.txt`
2. Wait for installation to complete
3. Try again

### Problem: "ModuleNotFoundError: No module named '_ctypes'"
**Solution (Mac/Linux only):**
```bash
pip install --upgrade ctypes
```

### Problem: Very Slow Response (> 15 minutes)
**Solutions:**
1. Check internet connection
2. Check if your Mistral account has credits left
3. Try again with simpler business idea input

### Problem: "Error: Invalid API Key"
**Solution:**
1. Go to https://console.mistral.ai
2. Check if your key is still valid
3. Create a new key if needed
4. Update `.env` file with new key

### Problem: "FAISS index error"
**Solution:**
```bash
# Reinstall FAISS
pip install --upgrade faiss-cpu
```

---

## 🎓 Understanding the Output

### Market Research Section
- Market size in Rs/USD
- Target customer profile
- Current market trends
- Demand analysis

### Competitor Analysis
- Who are your main competitors
- Their strengths and weaknesses
- How you can differentiate
- Pricing benchmarks

### Financial Plan
- Startup costs (equipment, inventory, setup)
- Monthly operating expenses
- Revenue projections (3 months, 6 months, 1 year)
- Break-even point
- Profitability forecast

### Risk Analysis
- Financial risks (cash flow, losses)
- Market risks (low demand)
- Operational risks (supply chain)
- Legal/regulatory requirements (licenses, compliance)
- How to mitigate each risk

### Marketing Strategy
- Brand positioning
- Target audience
- Marketing channels to use
- 90-day launch roadmap
- Customer retention strategies
- Marketing budget allocation

### Final Report
All of the above synthesized into a professional business plan you can:
- Share with investors
- Use to start your business
- Present to stakeholders
- Get feedback on

---

## 🔄 Running Again

To generate another business plan:
```bash
python main.py
```

Type a different business idea. Each run generates a new plan file.

---

## 💡 Tips & Tricks

### Tip 1: Be Specific with Your Business Idea
**Bad:** "I want to start a business"
**Good:** "I want to open a premium coffee shop in Delhi targeting remote workers"

### Tip 2: Save Your Plans
Output files are saved in `outputs/` folder. Keep them for reference.

### Tip 3: Iterate on Ideas
Run multiple times with different ideas to compare opportunities.

### Tip 4: Use for Business Decisions
- Share with co-founders
- Present to potential investors
- Use for bank loan applications
- Guide your actual business planning

### Tip 5: Customize for Your Industry
Edit files in `agents/` folder to customize prompts for specific industries.

---

## 📞 Getting Help

If you get stuck:
1. Check the error message carefully
2. Look for your error in the Troubleshooting section
3. Check Mistral docs: https://docs.mistral.ai
4. Check Python version: `python --version`
5. Check requirements installed: `pip list`

---

## 🎉 You're All Set!

Your autonomous business analyst is ready to help you plan any business idea.

**Next Steps:**
1. Run: `python main.py`
2. Type your business idea
3. Get your complete business plan in 5-10 minutes!

Happy planning! 🚀
