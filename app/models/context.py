from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class MarketContext:
    """Class to get the context market."""
    stock: int
    current_price: Decimal
    previous_price: Decimal
    price_change: Decimal
    iteration: int


@dataclass(frozen=True)
class AgentContext:
    market_context: MarketContext
    name: str
    politic: str
    balance: Decimal
    cards: int