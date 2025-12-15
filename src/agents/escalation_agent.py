import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))


from langgraph.types import Command
from services.llm_services import call_gemini as model
from src.AgentState import AgentState


class EscalationAgent:

    def __init__(self):
        
        self.model = model
        
    def escalation_decision(self, state: AgentState) -> Command:
        """Decide if human escalation is needed"""
        needs_escalation = (
            state["confidence_score"] < 0.6 or 
            state["urgency_level"] == "high"
        )
        
        state["human_escalation_required"] = needs_escalation
        
        if needs_escalation:
            return Command(goto="human_review")
        else:
            return Command(goto="response_generator")