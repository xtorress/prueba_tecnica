import pytest

from models.agents import Agent
from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic 

# @pytest.fixture
# def RandomAgent():
#     return RandomPolitic()

def test_random_politic_action():
    politic = RandomPolitic()
    agent1 = Agent("a1", politic)
    action = agent1.action(0.8)
    assert action in ["BUY", "SELL", "PASS"]

def test_trend_politic_action():
    politic = TrendPolitic()
    agent1 = Agent("a1", politic)
    action = agent1.action(0.8)
    assert action in ["BUY", "PASS"]

def test_anti_trend_politic_action():
    politic = AntiTrendPolitic()
    agent1 = Agent("a1", politic)
    action = agent1.action(-0.8)
    assert action in ["SELL", "PASS"]