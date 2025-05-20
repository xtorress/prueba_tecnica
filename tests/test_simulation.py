import pytest

from services.simulation import Simulation
from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic

@pytest.fixture
def simulation():
    return Simulation(start_price=200,
                      n_random_agents=5,
                      n_trend_agents=3,
                      n_anti_trend_agents=3,
                      iterations=5)

def test_create_agents(simulation):
    n_agents = 11
    random_count = sum(1 for agent in simulation.agents if isinstance(agent.politic, RandomPolitic))
    trend_count = sum(1 for agent in simulation.agents if isinstance(agent.politic, TrendPolitic))
    anti_trend_count = sum(1 for agent in simulation.agents if isinstance(agent.politic, AntiTrendPolitic))
    assert n_agents == len(simulation.agents)
    assert random_count == 5
    assert trend_count == 3
    assert anti_trend_count == 3
