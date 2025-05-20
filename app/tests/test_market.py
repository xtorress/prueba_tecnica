import pytest

from models.market import Market

@pytest.fixture
def TheMarket():
    return Market(200, 15)

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

def test_get_change_price(TheMarket):
    pass

def test_update_market(TheMarket):
    pass