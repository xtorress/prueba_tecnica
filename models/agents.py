from abc import ABC, abstractmethod
from enum import Enum
import random

from models.politics import Politic

class Agent():
    def __init__(self, name:str, politic: Politic):
        self.name = name
        self.politic = politic
        self.balance = 1000
        self.cards = 0


    def action(self, change_price: float):
        return self.politic.action(change_price)


