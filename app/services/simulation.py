import random

from models.agents import Agent
from models.market import Market
from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic
from logging_config import setup_logger

logger = setup_logger(__name__)

class Simulation():
    """Class for simulation."""
    def __init__(self,
                n_random_agents: int = 51,
                n_trend_agents: int = 24,
                n_anti_trend_agents: int = 24,
                n_personal_agents: int = 1,
                iterations: int = 1000):
        self.market = Market()
        self.agents: dict[Agent] = []
        self.iterations = iterations

        # Create agents
        agent_id = 0
        
        for _ in range(n_random_agents):
            agent_id += 1
            self.agents.append(Agent(f"AR-{agent_id}", RandomPolitic()))
        
        for _ in range(n_trend_agents):
            agent_id += 1
            self.agents.append(Agent(f"AT-{agent_id}", TrendPolitic()))

        for _ in range(n_anti_trend_agents):
            agent_id += 1
            self.agents.append(Agent(f"AAT-{agent_id}", AntiTrendPolitic()))
        
        for _ in range(n_personal_agents):
            agent_id += 1
            self.personal_agent = Agent(f"APP-{agent_id}", PersonalPolitic(self.iterations))
            self.agents.append(self.personal_agent)


    def run(self):
        for i in range(self.iterations):
            logger.info(f"Iteration {i} - Precio {self.market.current_price}")
            random.shuffle(self.agents)
            for agent in self.agents:
                agent.take_action(self.market)
            logger.info(f"Agent personal: {self.personal_agent.balance}, " \
                            f"p_tarjeta: {self.market.current_price}, " \
                            f"n_tarjeta: {self.personal_agent.cards}")
            self.market.update_market()
        logger.info(f"Agent perosonal: {self.personal_agent.balance}, cards: {self.personal_agent.cards}")
