from abc import abstractmethod, ABC
from decimal import Decimal
import random

from logging_config import setup_logger

logger = setup_logger(__name__)

class Market:
    PRICE_INCREASE = Decimal('1.005')
    PRICE_DECREASE = Decimal('0.995')

    def __init__(self, start_price=200, stock=100000):
        # self.start_price = start_price
        self.stock: int = stock
        self.current_price: Decimal = Decimal(str(start_price))
        self.previous_price: Decimal = Decimal(str(start_price))

    def buy_card(self):
        """
        Process the purchase of a graphics card
        """
        if self.stock <= 0:
            logger.warning("No hay stock.")
            return -1

        self.stock -= 1
        self.current_price *= self.PRICE_INCREASE
        return 1

    def sell_card(self):
        """
        Process the sale of a graphics card.
        """
        self.stock += 1
        self.current_price *= self.PRICE_DECREASE
        return 1

    def get_change_price(self) -> float:
        return ((self.current_price - self.start_price) / self.start_price)
    
    def update_market(self):
        self.previous_price = self.current_price