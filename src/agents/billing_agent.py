import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.llm_services import call_gemini as model
from src.AgentState import AgentState

class BillingAgent:
    
    def __init__(self):
        self.model = model


    def billing_agent(self, state: AgentState) -> AgentState:

        """Billing Agent to assist customers with billing inquiries"""


        # prompt = f"""You are a knowledgeable billing support agent. Provide a clear and accurate response to the following billing inquiry:
        # {state['customer_query']}"""

        # response = model(prompt, model="gemini-2.5-flash")

        response = "For billing issues, please check your account statement online or contact our billing department"

        state["agent_responses"]["billing"] = response
        
        return state