from abc import abstractmethod, ABC
from decimal import Decimal
import random

from logging_config import setup_logger

logger = setup_logger(__name__)

class Market:
    """Market class. Represents the graphics card market"""
    PRICE_INCREASE = Decimal('1.005')
    PRICE_DECREASE = Decimal('0.995')

    def __init__(self, start_price=200, stock=100000):
        self._stock: int = stock
        self._current_price: Decimal = Decimal(str(start_price))
        self._previous_price: Decimal = Decimal(str(start_price))

    @property
    def stock(self) -> int:
        return self._stock
    
    @property
    def current_price(self) -> Decimal:
        return self._current_price
    
    @property
    def previous_price(self) -> Decimal:
        return self._previous_price
    
    def _adjust_price(self, percent: Decimal) -> None:
        self._current_price *= percent

    def buy_card(self) -> bool:
        """
        Process the purchase of a graphics card
        """
        if self._stock <= 0:
            logger.warning("No hay stock.")
            return False

        self._stock -= 1
        self._adjust_price(self.PRICE_INCREASE)
        return True

    def sell_card(self) -> bool:
        """
        Process the sale of a graphics card.
        """
        self._stock += 1
        self._adjust_price(self.PRICE_DECREASE)
        return True

    def get_change_price(self) -> Decimal:
        """
        Calculates the change in price with respect to the previous iteration.
        """
        if self.previous_price == 0:
            logger.warning('Precio es 0.')
            return Decimal('0.000')
        return round((self._current_price - self._previous_price) / self._previous_price, 3)
    
    def update_market(self):
        self._previous_price = self._current_price