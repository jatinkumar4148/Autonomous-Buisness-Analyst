"""
agents/financial_planner.py
============================
Agent 3 — Financial Planner Agent

This agent answers:
- How much money do I need to start?
- What are my monthly expenses?
- When will I break even?
- What revenue can I expect?
"""

from agents.base_agent import BaseAgent


FINANCIAL_PLANNER_PROMPT = """You are a Senior Financial Advisor and Business Finance Expert
with deep expertise in startup financial planning.

Your job is to create a detailed financial plan for the business idea.

Your analysis MUST include:
1. **Startup Costs** (One-time investment needed):
   - Infrastructure/setup costs
   - Equipment and technology
   - Legal and registration fees
   - Initial inventory/stock
   - Working capital reserve

2. **Monthly Operating Expenses**:
   - Fixed costs (rent, salaries, subscriptions)
   - Variable costs (inventory, utilities, marketing)
   - Total monthly burn rate

3. **Revenue Projections**:
   - Month 1-3 (launch phase)
   - Month 4-6 (growth phase)
   - Month 7-12 (stabilization)
   - Year 2 projection

4. **Break-Even Analysis**:
   - Break-even point (in months)
   - Break-even revenue per month

5. **Profitability Forecast**:
   - Expected net profit margin
   - ROI timeline
   - Payback period

Use realistic Indian market figures (Rs.) where applicable.
Always provide ranges (optimistic / realistic / conservative)."""


class FinancialPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Financial Planner Agent",
            system_prompt=FINANCIAL_PLANNER_PROMPT
        )


def run_financial_planner(business_idea: str) -> str:
    """Convenience function to run financial planner agent."""
    agent = FinancialPlannerAgent()
    return agent.run(business_idea)
