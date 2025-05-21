from abc import abstractmethod, ABC
from decimal import Decimal
import random

class Politic(ABC):
    """Abstract class of politics."""

    @abstractmethod
    def action(self, change_price: Decimal):
        pass


class RandomPolitic(Politic):
    """Class for random agent policies."""

    def action(self, change_price: Decimal) -> str:
        return random.choices(["BUY", "SELL", "PASS"])[0]


class TrendPolitic(Politic):
    """Class for tresnd agent policies."""
    
    def action(self, change_price: Decimal):
        if change_price >= 0.01:
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class AntiTrendPolitic(Politic):
    """Class for anti trend agent policies."""

    def action(self, change_price: Decimal):
        if change_price <= -0.01:
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class PersonalPolitic(Politic):
    """Class of policy for agent with logic defined by me."""

    def action(self, change_price: Decimal):
        pass
