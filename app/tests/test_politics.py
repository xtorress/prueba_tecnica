import pytest
from decimal import Decimal
from unittest.mock import patch, MagicMock
from dataclasses import FrozenInstanceError

from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic
from models.market import MarketContext
from models.agents import AgentContext

# def test_random_politic_returns_valid_action():
#     policy = RandomPolitic()

#     action = policy.action(price_change=0.05)

#     assert action in ["BUY", "SELL", "PASS"], f"{action}"

def create_market_context(price_change = Decimal('0.005')):
    return MarketContext(
        stock=4,
        current_price=200,
        previous_price=199,
        price_change=price_change,
        iteration=10
    )

def test_market_context_is_immutable():
    context = create_market_context()
    with pytest.raises(FrozenInstanceError):
        context.price_change = Decimal('0.001')

def test_politic_name():
    policy = AntiTrendPolitic()
    assert policy.__str__() == 'AntiTrendPolitic'

def test_trend_politic_buy_when_positive_trend():
    market_context = create_market_context(Decimal('0.01'))
    policy = TrendPolitic()
    agent_context = AgentContext(market_context, 'a1', str(policy), Decimal('100'), 5)
    action = policy.action(agent_context)
    assert action in ["BUY", "PASS"]

def test_trend_politic_sell_when_not_trending():
    market_context = create_market_context(Decimal('0.005'))
    policy = TrendPolitic()
    agent_context = AgentContext(market_context, 'a1', str(policy), Decimal('100'), 5)
    action = policy.action(agent_context)
    assert action in ["PASS", "SELL"]

def test_antitrend_politic_buy_when_negative_trend():
    market_context = create_market_context(Decimal('-0.01'))
    policy = AntiTrendPolitic()
    agent_context = AgentContext(market_context, 'a1', str(policy), Decimal('100'), 5)
    action = policy.action(agent_context)
    assert action in ["BUY", "PASS"]

def test_antitrend_politic_sell_when_positive_trend():
    market_context = create_market_context(Decimal('0.02'))
    policy = AntiTrendPolitic()
    agent_context = AgentContext(market_context, 'a1', str(policy), Decimal('100'), 5)
    action = policy.action(agent_context)
    assert action in ["PASS", "SELL"]

# test personal agent