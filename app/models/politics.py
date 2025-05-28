from abc import abstractmethod, ABC
from decimal import Decimal
import random

from models.context import AgentContext
from logging_config import setup_logger

logger = setup_logger(__name__)

class Politic(ABC):
    """Abstract class of politics."""

    @abstractmethod
    def action(self, agent_context):
        pass


class RandomPolitic(Politic):
    """Class for random agent policies."""

    def action(self, agent_context: AgentContext) -> str:
        return random.choices(["BUY", "SELL", "PASS"])[0]


class TrendPolitic(Politic):
    """Class for tresnd agent policies."""
    
    def action(self, agent_context: AgentContext):
        if agent_context.market_context.price_change >= Decimal('0.01'):
            return random.choices(["BUY", "PASS"], weights=[0.75, 0.25])[0]
        else:
            return random.choices(["PASS", "SELL"], weights=[0.8, 0.2])[0]


class AntiTrendPolitic(Politic):
    """Class for anti trend agent policies."""

    def action(self, agent_context: AgentContext):
        if agent_context.market_context.price_change <= Decimal('-0.01'):
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
    
    def action(self, agent_context: AgentContext):
        price_change_market = agent_context.market_context.price_change 
        price_change_trend = self._trend_price(price_change_market)
        
        if agent_context.market_context.iteration <= 10:
            return "BUY"
        
        if self._is_max_cards(agent_context):
            return "SELL"

        if price_change_trend <= 0 and price_change_market <= -0.01:   
            return "BUY"
        elif price_change_trend > 0 and price_change_market >= 0.01:
            return "SELL"
        else:
            return "PASS"
        
    def _trend_price(self, price):
        self._current_iteration += 1
        self._price_trend.append(price)

        if len(self._price_trend) == self._size_trend_list:
            self._price_trend.pop(0)
            return sum(self._price_trend)
        else:
            return 0
        
    def _is_max_cards(self, agent: AgentContext):
        if self.n_iterations - agent.market_context.iteration <= agent.cards + 1:
            return True
        return False