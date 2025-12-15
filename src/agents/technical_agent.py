
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.AgentState import AgentState
from services.llm_services import call_gemini as model

class TechnicalAgent:

    def __init__(self):

        self.model = model

    def technical_agent(self, state: AgentState ) -> AgentState:

        """Technical Support Agent to assist customers with technical issues"""

        # prompt = f"""You are a skilled technical support agent. Provide a clear and detailed solution to the following technical issue:
        # {state['customer_query']}"""

        # response = self.model(prompt, model="gemini-2.5-flash")

        response = "Please try restarting your device and ensure that you have the latest software updates installed."

        state["agent_responses"]["technical"] = response

        return state