from typing import List

from models.agents import Agent
from models.politics import PersonalPolitic


class GenerateReport:
    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def get_top5_agents(self):
        top5 = sorted(self.agents, 
                      key=lambda agent: agent.balance, 
                      reverse=True)[:5]
        print("\nTOP 5 DE AGENTES CON MAYOR BALANCE\n")
        print(f"{'Nombre':<10} \t{'Política':<20} {'Balance':>10} \tTarjetas")
        for agent in top5:
            print(f"{agent.name:<10} \t{str(agent.politic):<20} {agent.balance:>10} \t{agent.cards}")

    def info_personal_agent(self):
        my_agent = None
        for agent in self.agents:
            if isinstance(agent.politic, PersonalPolitic):
                my_agent = agent
        print('-'*33)
        print(f'|AGENTE PERSONAL: {my_agent.name} \t|')
        print('-'*33)
        print(f'| BALANCE:\t{my_agent.balance} \t|')
        print(f'| TARJETAS:\t{my_agent.cards} \t\t|')
        print('-'*33)

