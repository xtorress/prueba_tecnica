from decimal import Decimal, ROUND_HALF_UP

from models.context import MarketContext
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
        self._price_change: Decimal = 0.000
        self._iteration: int = 0

    @property
    def stock(self) -> int:
        return self._stock
    
    @property
    def current_price(self) -> Decimal:
        return self._current_price
    
    @current_price.setter
    def current_price(self, new_price):
        if not isinstance(new_price, Decimal):
            new_price = Decimal(str(new_price))
        self._current_price = new_price.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
    
    @property
    def previous_price(self) -> Decimal:
        return self._previous_price
    
    @property
    def price_change(self) -> Decimal:
        return self._price_change
    
    @price_change.setter
    def price_change(self, p_change):
        if not isinstance(p_change, Decimal):
            p_change = Decimal(str(p_change))
        self._price_change = p_change.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
    
    @property
    def iteration(self) -> int:
        return self._iteration
    
    def _adjust_price(self, percent: Decimal) -> None:
        self.current_price *= percent

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
        # Agregar atributo self._account = 0, para un flujo correcto de mercado
        # validar si el mercado tiene saldo self.account > self.current_price
        self._stock += 1
        self._adjust_price(self.PRICE_DECREASE)
        return True

    def _get_change_price(self) -> Decimal:
        """
        Calculates the change in price with respect to the previous iteration.
        """
        if self.previous_price == 0:
            logger.warning('Precio es 0.')
            return Decimal('0.000')
        result = (self.current_price- self._previous_price) / self._previous_price
        return Decimal(str(result)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
    
    def get_context(self) -> MarketContext:
        """
        Method to send the market context at the beginning of the iteration.
        """
        return MarketContext(
            self.stock,
            self.current_price, 
            self.previous_price, 
            self.price_change, 
            self.iteration
            )

    def update_market(self):
        """
        Update the market.
        """
        self.price_change = self._get_change_price()
        self._previous_price = self.current_price
        self._iteration += 1