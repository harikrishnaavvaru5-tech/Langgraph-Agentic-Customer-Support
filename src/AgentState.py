from typing import TypedDict



# ============ AGENT STATE DEFINITION ============
class AgentState(TypedDict):
    customer_query: str
    intent: str
    urgency_level: str  # "low", "medium", "high"
    confidence_score: float
    agent_responses: dict
    human_escalation_required: bool
    human_feedback: str
    final_response: str
    conversation_history: list