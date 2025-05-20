import pytest
import random
from unittest.mock import patch, MagicMock

from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic
from models.market import Market

@pytest.fixture
def Marketplace():
    return Market(stock=10)

# def test_random_politic_returns_valid_action():
#     policy = RandomPolitic()

#     action = policy.action(change_price=0.05)

#     assert action in ["BUY", "SELL", "PASS"], f"{action}"

def test_trend_politic_buy_when_positive_trend():
    market = MagicMock()
    market.get_change_price.return_value = 0.01
    policy = TrendPolitic()
    action = policy.action(market)
    assert action in ["BUY", "PASS"]

def test_trend_politic_sell_when_not_trending():
    market = MagicMock()
    market.get_change_price.return_value = 0.005
    policy = TrendPolitic()
    action = policy.action(market)
    assert action in ["PASS", "SELL"]

def test_antitrend_politic_buy_when_negative_trend():
    market = MagicMock()
    market.get_change_price.return_value = -0.01
    policy = AntiTrendPolitic()
    action = policy.action(market)
    assert action in ["BUY", "PASS"]

def test_antitrend_politic_sell_when_positive_trend():
    market = MagicMock()
    market.get_change_price.return_value = 0.02
    policy = AntiTrendPolitic()
    action = policy.action(market)
    assert action in ["PASS", "SELL"]

# test personal agent