from abc import ABC, abstractmethod
from enum import Enum
import random

from models.market import Politic

class Agent():
    def __init__(self, name:str, politic: Politic):
        self.name = name
        self.politic = politic

    def action(self, change_price: float):
        return self.politic.action(change_price)
