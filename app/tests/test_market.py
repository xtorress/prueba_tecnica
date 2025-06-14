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

def test_buy_card_no_stock(TheMarket):
    TheMarket._stock = 0
    TheMarket.buy_card()
    assert TheMarket.stock == 0
    assert TheMarket.current_price == 200

def test_sell_card(TheMarket):
    TheMarket.sell_card()
    assert TheMarket.stock == 16
    assert TheMarket.current_price == 199

def test_get_change_price_down(TheMarket):
    TheMarket._previous_price = Decimal('201')
    TheMarket._current_price = Decimal('200')
    result = TheMarket._get_change_price()
    assert result == Decimal('-0.005')

def test_get_change_price_up(TheMarket):
    TheMarket._previous_price = Decimal('199')
    TheMarket._current_price = Decimal('200')
    result = TheMarket._get_change_price()
    assert result == Decimal('0.005')

def test_get_change_price_equal(TheMarket):
    TheMarket._previous_price = Decimal('200')
    TheMarket._current_price = Decimal('200')
    result = TheMarket._get_change_price()
    assert result == Decimal('0.00')

def test_update_market(TheMarket):
    TheMarket._previous_price = Decimal('200')
    TheMarket._current_price = Decimal('199')
    TheMarket.update_market()
    assert TheMarket.price_change == Decimal('-0.005')
    assert TheMarket.previous_price == Decimal('199')

def test_get_context(TheMarket):
    context = TheMarket.get_context()
    assert context.stock == 15
    assert context.current_price == 200
    assert context.previous_price == 200
    assert context.price_change == 0.000
    assert context.iteration == 0