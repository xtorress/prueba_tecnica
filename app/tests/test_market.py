import pytest
from decimal import Decimal

from models.market import Market

@pytest.fixture
def TheMarket():
    return Market(200, 15)

def test_adjust_price(TheMarket):
    percent = Decimal('1.005')
    TheMarket._adjust_price(percent)
    assert TheMarket.current_price == 201

def test_buy_card(TheMarket):
    TheMarket.buy_card()
    assert TheMarket.stock == 14
    assert TheMarket.current_price == 201

def test_sell_card(TheMarket):
    TheMarket.sell_card()
    assert TheMarket.stock == 16
    assert TheMarket.current_price == 199

def test_sell_card_no_stock(TheMarket):
    pass

def test_get_change_price_down(TheMarket):
    TheMarket._previous_price = Decimal('201')
    TheMarket._current_price = Decimal('200')
    result = TheMarket.get_change_price()
    assert result == Decimal('-0.005')

def test_get_change_price_up(TheMarket):
    TheMarket._previous_price = Decimal('199')
    TheMarket._current_price = Decimal('200')
    result = TheMarket.get_change_price()
    assert result == Decimal('0.005')

def test_get_change_price_up(TheMarket):
    TheMarket._previous_price = Decimal('200')
    TheMarket._current_price = Decimal('200')
    result = TheMarket.get_change_price()
    assert result == Decimal('0.00')

def test_update_market(TheMarket):
    pass