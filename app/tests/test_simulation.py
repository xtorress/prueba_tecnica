import pytest
from unittest.mock import MagicMock, patch

from services.simulation import Simulation
from models.market import Market
from models.agents import Agent
from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic

@pytest.fixture
def simulation():
    return Simulation(n_random_agents=5,
                      n_trend_agents=3,
                      n_anti_trend_agents=3,
                      n_personal_agents=1,
                      iterations=5)

def test_create_agents(simulation):
    n_agents = 12
    random_count = sum(1 for agent in simulation.agents if isinstance(agent.politic, RandomPolitic))
    trend_count = sum(1 for agent in simulation.agents if isinstance(agent.politic, TrendPolitic))
    anti_trend_count = sum(1 for agent in simulation.agents if isinstance(agent.politic, AntiTrendPolitic))
    assert n_agents == len(simulation.agents)
    assert random_count == 5
    assert trend_count == 3
    assert anti_trend_count == 3


def test_simulation_initial_agent_count():
    """Test that the correct number of agents are created."""
    sim = Simulation(n_random_agents=10, n_trend_agents=5, n_anti_trend_agents=5, n_personal_agents=1)

    assert len(sim.agents) == 21
    assert isinstance(sim.market, Market)
    assert sim.iterations == 1000  # default

    # Check agent naming convention
    assert sim.agents[0].name.startswith("AR-")
    assert sim.agents[10].name.startswith("AT-")
    assert sim.agents[15].name.startswith("AAT-")


@patch("services.simulation.Agent")
def test_simulation_run_calls_take_action(mock_agent_class):
    """Test that agent.take_action is called for each agent in each iteration."""
    # Create dummy agent mock
    dummy_agent = MagicMock()
    mock_agent_class.return_value = dummy_agent

    # Setup simulation with small numbers
    sim = Simulation(n_random_agents=2, n_trend_agents=1, n_anti_trend_agents=1, n_personal_agents=1, iterations=3)
    
    sim.run()

    # Assert that take_action was called 4 agents * 3 iterations
    assert dummy_agent.take_action.call_count == 15


def test_simulation_market_updates(monkeypatch):
    """Test that the market's update_market method is called."""
    sim = Simulation(n_random_agents=1, n_trend_agents=0, n_anti_trend_agents=0, iterations=2)

    # Spy on the market method
    sim.market.update_market = MagicMock()

    # Replace agent behavior to prevent side effects
    for agent in sim.agents:
        agent.take_action = MagicMock()

    sim.run()

    assert sim.market.update_market.call_count == 2