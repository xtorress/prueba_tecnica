import pytest
from decimal import Decimal
from unittest.mock import MagicMock

from models.agents import Agent
from models.politics import Politic

class DummyPolitic:
    def __init__(self, action_return):
        self._action_return = action_return

    def action(self, price_change):
        return self._action_return

@pytest.fixture
def market_mock():
    market = MagicMock()
    market.current_price = Decimal('100')
    market.price_change = Decimal('0.01')
    return market

def test_buy_success(market_mock):
    politic = DummyPolitic("BUY")
    agent = Agent("TestAgent", politic)

    # Configuramos buy_card para que funcione (devuelva True)
    market_mock.buy_card.return_value = True

    result = agent.take_action(market_mock)

    assert result == "BUY"
    assert agent.cards == 1
    assert agent.balance == Decimal('900')  # 1000 - 100
    market_mock.buy_card.assert_called_once()

def test_buy_insufficient_balance(market_mock):
    politic = DummyPolitic("BUY")
    agent = Agent("TestAgent", politic)
    agent._balance = Decimal('50')  # Menor que current_price (100)

    result = agent.take_action(market_mock)

    assert result is None
    assert agent.cards == 0
    assert agent.balance == Decimal('50')
    market_mock.buy_card.assert_not_called()

def test_buy_no_stock(market_mock):
    politic = DummyPolitic("BUY")
    agent = Agent("TestAgent", politic)

    market_mock.buy_card.return_value = False

    result = agent.take_action(market_mock)

    assert result is None
    assert agent.cards == 0
    assert agent.balance == Decimal('1000')
    market_mock.buy_card.assert_called_once()

def test_sell_success(market_mock):
    politic = DummyPolitic("SELL")
    agent = Agent("TestAgent", politic)

    # Ponemos 1 tarjeta para poder vender
    agent._cards = 1
    market_mock.sell_card.return_value = True

    result = agent.take_action(market_mock)

    assert result == "SELL"
    assert agent.cards == 0
    assert agent.balance == Decimal('1100')  # 1000 + 100
    market_mock.sell_card.assert_called_once()

def test_sell_no_cards(market_mock):
    politic = DummyPolitic("SELL")
    agent = Agent("TestAgent", politic)
    agent._cards = 0

    result = agent.take_action(market_mock)

    assert result is None
    assert agent.cards == 0
    assert agent.balance == Decimal('1000')
    market_mock.sell_card.assert_not_called()

def test_sell_market_sell_card_false(market_mock):
    politic = DummyPolitic("SELL")
    agent = Agent("TestAgent", politic)
    agent._cards = 1
    market_mock.sell_card.return_value = False

    result = agent.take_action(market_mock)

    assert result == "SELL"
    assert agent.cards == 0
    assert agent.balance == Decimal('1100')
    market_mock.sell_card.assert_called_once()

def test_no_action(market_mock):
    politic = DummyPolitic("HOLD")  # Acción que no es BUY ni SELL
    agent = Agent("TestAgent", politic)

    result = agent.take_action(market_mock)

    assert result is None
    assert agent.cards == 0
    assert agent.balance == Decimal('1000')
    market_mock.buy_card.assert_not_called()
    market_mock.sell_card.assert_not_called()
