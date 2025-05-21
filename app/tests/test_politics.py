import pytest
from unittest.mock import patch, MagicMock

from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic

# def test_random_politic_returns_valid_action():
#     policy = RandomPolitic()

#     action = policy.action(change_price=0.05)

#     assert action in ["BUY", "SELL", "PASS"], f"{action}"

def test_trend_politic_buy_when_positive_trend():
    change_price = 0.01
    policy = TrendPolitic()
    action = policy.action(change_price)
    assert action in ["BUY", "PASS"]

def test_trend_politic_sell_when_not_trending():
    change_price = 0.005
    policy = TrendPolitic()
    action = policy.action(change_price)
    assert action in ["PASS", "SELL"]

def test_antitrend_politic_buy_when_negative_trend():
    change_price = -0.01
    policy = AntiTrendPolitic()
    action = policy.action(change_price)
    assert action in ["BUY", "PASS"]

def test_antitrend_politic_sell_when_positive_trend():
    change_price = 0.02
    policy = AntiTrendPolitic()
    action = policy.action(change_price)
    assert action in ["PASS", "SELL"]

# test personal agent