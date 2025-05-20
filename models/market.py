from abc import abstractmethod, ABC
import random

from models.card import GraphicCard

class Market:
    def __init__(self, start_price=200, stock=100):
        self.start_price = start_price
        self.stock = stock
        self.current_price = start_price

    def buy_card():
        pass

    def sell_card():
        pass

    def get_change_price(self) -> float:
        return ((self.current_price - self.start_price) / self.start_price)