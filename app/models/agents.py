from abc import ABC, abstractmethod
from enum import Enum
from decimal import Decimal
import random

from models.politics import Politic
from models.market import Market
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
    
    @property
    def cards(self) -> int:
        return self._cards
    
    # def action(self, market: Market):
    #     return self.politic.action(market)
    
    def take_action(self, market: Market):
        market_context = market.get_context()
        action = self._politic.action(market_context)
        if action == "BUY":
            return self._buy_card(market)
        elif action == "SELL":
            return self._sell_card(market)
        else:
            logger.info(f"Agente {self.name} no hizo nada.")
            return None

    def _buy_card(self, market: Market):
        if self.balance < market.current_price:
            logger.info(f"Agente {self.name} no tiene balance suficiente.")
            return None
        
        if not market.buy_card():
            logger.info(f"Agente {self.name} no pudo comprar, tienda sin stock.")
            return None
        
        self._balance -= market.current_price
        self._cards += 1
        logger.info(f"Agente {self.name} compro una tarjeta a {market.current_price}")
        return "BUY"

    def _sell_card(self, market: Market):
        if self.cards <= 0:
            logger.info(f"Agente {self.name} no tiene tarjetas para vender.")
            return None

        if not market.sell_card():
            logger.info(f"Falta agregar atributo dinero a Market")

        self._balance += market.current_price
        self._cards -= 1
        return "SELL"        


# class PersonalAgent(Agent):
#     pass