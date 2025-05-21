from abc import abstractmethod, ABC
from decimal import Decimal
import random

class Politic(ABC):
    """Abstract class of politics."""

    @abstractmethod
    def action(self, price_change: Decimal):
        pass


class RandomPolitic(Politic):
    """Class for random agent policies."""

    def action(self, price_change: Decimal) -> str:
        return random.choices(["BUY", "SELL", "PASS"])[0]


class TrendPolitic(Politic):
    """Class for tresnd agent policies."""
    
    def action(self, price_change: Decimal):
        if price_change >= 0.01:
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class AntiTrendPolitic(Politic):
    """Class for anti trend agent policies."""

    def action(self, price_change: Decimal):
        if price_change <= -0.01:
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class PersonalPolitic(Politic):
    """Class of policy for agent with logic defined by me."""

    def __init__(self, n_iterations):
        self.n_iterations: int = n_iterations
        self._current_iteration: int = 0
        self._price_trend = []
        self._size_trend_list = 4
    
    def action(self, price_change: Decimal):

        price_change_trend = 0
        if self.trend_price(price_change):
            price_change_trend = sum(self._price_trend)

        if price_change_trend < 0 and price_change <= -0.01:   
            return "BUY"
        elif price_change_trend > 0 and price_change >= 0.01:
            return "SELL"
        else:
            return "PASS"
        
    def trend_price(self, price):
        self._current_iteration += 1
        self._price_trend.append(price)

        if len(self._price_trend) == self._size_trend_list:
            self._price_trend.pop(0)
            return True
        else:
            return False