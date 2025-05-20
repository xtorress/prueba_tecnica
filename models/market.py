from abc import abstractmethod, ABC
import random

from models.card import GraphicCard

class Market:
    def __init__(self, start_price=200, stock=100):
        self.start_pice = start_price
        self.stock = stock

    def init_market():
        pass