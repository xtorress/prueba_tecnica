from abc import abstractmethod, ABC
import random

from logging_config import setup_logger

logger = setup_logger(__name__)

class Market:
    def __init__(self, start_price=200, stock=15):
        self.start_price = start_price
        self.stock = stock
        self.current_price = start_price
        self.previous_price = start_price

    def buy_card(self):
        self.stock += 1
        self.current_price -= 0.005 * self.current_price

    def sell_card(self):
        if self.stock > 0:
            self.stock -= 1
            self.current_price += 0.005 * self.current_price
            return True
        else:
            logger.warning("No hay stock.")
            return False

    def get_change_price(self) -> float:
        return ((self.current_price - self.start_price) / self.start_price)
    
    def update_market(self):
        self.previous_price = self.current_price