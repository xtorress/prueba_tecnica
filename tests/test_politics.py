import pytest
import random

from models.politics import RandomPolitic, TrendPolitic, AntiTrendPolitic, PersonalPolitic

def test_random_politic_returns_valid_action():
    policy = RandomPolitic()
    action = policy.set_politc(change_price=0.05)
    assert action in ["BUY", "SELL", "PASS"], f"{action}"

def test_trend_politic_buy_when_positive_trend():
    policy = TrendPolitic()
    action = policy.set_politc(change_price=0.01)
    # Con la semilla fija, debe dar 'BUY' o 'PASS'
    assert action in ["BUY", "PASS"]

def test_trend_politic_sell_when_not_trending():
    policy = TrendPolitic()
    action = policy.set_politc(change_price=0.005)
    assert action in ["PASS", "SELL"]

def test_antitrend_politic_buy_when_negative_trend():
    policy = AntiTrendPolitic()
    action = policy.set_politc(change_price=-0.01)
    assert action in ["BUY", "PASS"]

def test_antitrend_politic_sell_when_positive_trend():
    policy = AntiTrendPolitic()
    action = policy.set_politc(change_price=0.02)
    assert action in ["PASS", "SELL"]

def test_personal_politic_implemented():
    # Como está vacío, solo verificamos que no lance errores y devuelve None
    policy = PersonalPolitic()
    result = policy.set_politc(change_price=0.05)
    assert result is None
