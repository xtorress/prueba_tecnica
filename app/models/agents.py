from abc import ABC, abstractmethod
from enum import Enum
import random

from models.politics import Politic
from models.market import Market
from logging_config import setup_logger

logger = setup_logger(__name__)

class Agent():
    def __init__(self, name:str, politic: Politic):
        self.name = name
        self.politic = politic
        self.balance = 1000
        self.init_balance = 1000
        self.cards = 0

    # def action(self, market: Market):
    #     return self.politic.action(market)

    def take_action(self, market: Market):
        action = self.politic.action(market.price_change)
        if action == "BUY" and self.balance >= market.current_price:
            if market.sell_card():
                self.balance -= market.current_price
                self.cards += 1
                logger.info("Agente compro tarjeta.")
            else:
                logger.warning("No se pudo comprar. 1) no money 2) no stock in marketplace")
                pass
        elif action == "SELL":
            if self.cards > 0:
                self.balance += market.current_price
                self.cards -= 1
                market.buy_card()
                logger.info("Agente vendio tarjeta.")
            else:
                logger.warning("No tiene tarjetas para vender.")
        else:
            logger.info("Agente no hizo nada.")
    

