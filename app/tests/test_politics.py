import pytest
from decimal import Decimal
from unittest.mock import patch, MagicMock

from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic
from models.market import MarketContext

# def test_random_politic_returns_valid_action():
#     policy = RandomPolitic()

#     action = policy.action(price_change=0.05)

#     assert action in ["BUY", "SELL", "PASS"], f"{action}"

@pytest.fixture
def GetMarketContext():
    return MarketContext(
        stock=4,
        current_price=200,
        previous_price=199,
        price_change=0.005,
        iteration=10
    )

def test_trend_politic_buy_when_positive_trend(GetMarketContext):
    GetMarketContext.price_change = Decimal('0.01')
    policy = TrendPolitic()
    action = policy.action(GetMarketContext)
    assert action in ["BUY", "PASS"]

def test_trend_politic_sell_when_not_trending(GetMarketContext):
    GetMarketContext.price_change = Decimal('0.005')
    policy = TrendPolitic()
    action = policy.action(GetMarketContext)
    assert action in ["PASS", "SELL"]

def test_antitrend_politic_buy_when_negative_trend(GetMarketContext):
    GetMarketContext.price_change = Decimal('-0.01')
    policy = AntiTrendPolitic()
    action = policy.action(GetMarketContext)
    assert action in ["BUY", "PASS"]

def test_antitrend_politic_sell_when_positive_trend(GetMarketContext):
    GetMarketContext.price_change = Decimal('0.02')
    policy = AntiTrendPolitic()
    action = policy.action(GetMarketContext)
    assert action in ["PASS", "SELL"]

# test personal agent