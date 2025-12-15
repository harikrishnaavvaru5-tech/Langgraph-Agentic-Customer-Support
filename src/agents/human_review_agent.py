import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))


from src.AgentState import AgentState
from services.llm_services import call_gemini as model

class HumanReviewAgent:

    def __init__(self):
        self.model = model


    # ============ HUMAN-IN-THE-LOOP NODE ============
    def human_review(self, state: AgentState) -> AgentState:
        
        """Human review & decision (with interrupt)"""

        print("\n⚠️  ESCALATION REQUIRED - Awaiting human review...")

        print(f"Query: {state['customer_query']}")
        print(f"Agent Responses: {state['agent_responses']}")
        
        # In production: use LangGraph's interrupt mechanism
        # This pauses execution and waits for human input
        human_input = input("👤 Human feedback: ")
        
        state["human_feedback"] = human_input

        return state