from dataclasses import dataclass
from enum import Enum
from decimal import Decimal, ROUND_HALF_UP
import random

from models.politics import Politic
from models.market import Market, MarketContext
from models.context import AgentContext
from logging_config import setup_logger

logger = setup_logger(__name__)

class Agent():
    def __init__(self, name:str, politic: Politic):
        self._name: str = name
        self._politic: Politic = politic
        self._balance: Decimal = Decimal('1000')
        self._cards: int = 0

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def balance(self) -> Decimal:
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        if not isinstance(new_balance, Decimal):
            new_balance = Decimal(str(new_balance))
        self._balance = new_balance.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

    @property
    def cards(self) -> int:
        return self._cards
    
    @property
    def politic(self) -> Politic:
        return self._politic
    
    def take_action(self, market: Market):
        agent_context = self._get_context(market.get_context())
        action = self._politic.action(agent_context)
        if action == "BUY":
            return self._buy_card(market)
        elif action == "SELL":
            return self._sell_card(market)
        else:
            logger.debug(f"Agente {self.name} no hizo nada.")
            return None

    def _buy_card(self, market: Market):
        if self.balance < market.current_price:
            logger.debug(f"Agente {self.name} no tiene balance suficiente.")
            return None
        
        cost = market.buy_card()
        if cost < 0:
            logger.debug(f"Agente {self.name} no pudo comprar, tienda sin stock.")
            return None
        
        self.balance -= cost
        self._cards += 1
        logger.debug(f"Agente {self.name} compro una tarjeta a {market.current_price}")
        return "BUY"

    def _sell_card(self, market: Market):
        if self.cards <= 0:
            logger.debug(f"Agente {self.name} no tiene tarjetas para vender.")
            return None
        
        income = market.sell_card()
        self._balance += income
        self._cards -= 1
        return "SELL"        

    def _get_context(self, market_context: MarketContext) -> AgentContext:
        return AgentContext(market_context, self.cards)
