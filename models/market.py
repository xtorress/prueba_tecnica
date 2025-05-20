from abc import abstractmethod, ABC
import random

from models.card import GraphicCard



class Politics(ABC):
    """Abstract class of politics."""

    @abstractmethod
    def set_politc(self, change_price):
        pass


class RandomPolitic(Politics):
    """Class for random agent policies."""

    def set_politc(self, change_price: float) -> str:
        return random.choices(["BUY", "SELL", "PASS"])[0]


class TrendPolitic(Politics):
    """Class for tresnd agent policies."""
    
    def set_politc(self, change_price):
        if change_price >= 0.01:
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class AntiTrendPolitic(Politics):
    """Class for anti trend agent policies."""

    def set_politc(self, change_price):
        if change_price <= -0.01:
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class PersonalPolitic(Politics):
    """Class of policy for agent with logic defined by me."""

    def set_politc(self, change_price):
        pass


    