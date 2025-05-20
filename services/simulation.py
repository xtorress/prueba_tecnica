from models.agents import Agent
from models.market import Market
from models.card import GraphicCard
from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic

import random

class Simulation():
    """Class for simulation."""
    def __init__(self,
                start_price: float = 200,
                #stock: int = 100000,
                n_random_agents: int = 51,
                n_trend_agents: int = 24,
                n_anti_trend_agents: int = 24,
                iterations: int = 1000):
        self.market = Market()
        self.agents: dict[Agent] = []
        self.iterations = iterations

        # Create agents
        agent_id = 0
        
        for _ in range(n_random_agents):
            self.agents.append(Agent(f"AR-{agent_id}", RandomPolitic()))
        
        for _ in range(n_trend_agents):
            self.agents.append(Agent(f"AT-{agent_id}", TrendPolitic()))

        for _ in range(n_anti_trend_agents):
            self.agents.append(Agent(f"AAT-{agent_id}", AntiTrendPolitic()))

    # def run(self):
    #     for i in self.iterations:
    #         random.shuffle(self.agents)
    #         for agent in self.agents:
    #             agent.action()
