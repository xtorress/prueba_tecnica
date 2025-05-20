import pytest
from unittest.mock import MagicMock

from models.agents import Agent
from models.politics import Politic

class DummyBuyPolitic(Politic):
    def action(self, market):
        return "BUY"

class DummySellPolitic(Politic):
    def action(self, market):
        return "SELL"

class DummyPassPolitic(Politic):
    def action(self, market):
        return "PASS"

# --- action method ---

def test_agent_action_returns_policy_action():
    market = MagicMock()
    policy = MagicMock()
    policy.action.return_value = "SELL"
    agent = Agent("A1", policy)

    result = agent.action(market)

    assert result == "SELL"
    policy.action.assert_called_once_with(market)


# --- take_action method ---

def test_agent_buys_card_if_enough_balance_and_stock():
    market = MagicMock()
    market.current_price = 100
    market.sell_card.return_value = True

    agent = Agent("Buyer", DummyBuyPolitic())
    agent.balance = 200
    agent.cards = 0

    agent.take_action(market)

    assert agent.balance == 100
    assert agent.cards == 1
    market.sell_card.assert_called_once()

def test_agent_does_not_buy_if_no_stock():
    market = MagicMock()
    market.current_price = 100
    market.sell_card.return_value = False

    agent = Agent("NoStockBuyer", DummyBuyPolitic())
    agent.balance = 200
    agent.cards = 0

    agent.take_action(market)

    assert agent.balance == 200  # no change
    assert agent.cards == 0
    market.sell_card.assert_called_once()

def test_agent_does_not_buy_if_not_enough_balance():
    market = MagicMock()
    market.current_price = 100
    market.sell_card.return_value = True

    agent = Agent("PoorBuyer", DummyBuyPolitic())
    agent.balance = 50  # not enough
    agent.cards = 0

    agent.take_action(market)

    assert agent.balance == 50
    assert agent.cards == 0
    market.sell_card.assert_not_called()


def test_agent_sells_card_if_has_card():
    market = MagicMock()
    market.current_price = 150

    agent = Agent("Seller", DummySellPolitic())
    agent.cards = 1
    agent.balance = 500

    agent.take_action(market)

    assert agent.balance == 650
    assert agent.cards == 0
    market.buy_card.assert_called_once()

def test_agent_does_not_sell_if_no_cards():
    market = MagicMock()
    market.current_price = 150

    agent = Agent("NoCards", DummySellPolitic())
    agent.cards = 0
    agent.balance = 500

    agent.take_action(market)

    assert agent.balance == 500
    assert agent.cards == 0
    market.buy_card.assert_not_called()


def test_agent_passes_does_nothing():
    market = MagicMock()
    market.current_price = 200

    agent = Agent("Passive", DummyPassPolitic())
    agent.cards = 5
    agent.balance = 300

    agent.take_action(market)

    assert agent.balance == 300
    assert agent.cards == 5
    market.sell_card.assert_not_called()
    market.buy_card.assert_not_called()
