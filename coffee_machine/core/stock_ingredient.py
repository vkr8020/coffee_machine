from threading import Lock
from coffee_machine.apputils import IngredientShortageException, IngredientInsufficientException

lock = Lock()


class StockIngredient:
    """
    This class is for handling the Inventory Ingredients
    """
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity
        self._min_quantity = 10 # if the current quantity is below this amount(10ml), raises a refill request

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def consume_quantity(self, amount):
        if amount <= self._quantity:
            lock.acquire()
            self._quantity = self._quantity - amount
            lock.release()
        else:
            raise IngredientInsufficientException
        if self._quantity < self._min_quantity:
            raise IngredientShortageException

    def add_quantity(self, amount):
        lock.acquire()
        self._quantity += amount
        lock.release()

    def is_consumable(self, amount):
        if amount > self._quantity:
            return 0
        else:
            return 1

    def __repr__(self):
        return "\"" + self._name + "\": " + str(self._quantity)

    def __str__(self):
        return "\"" + self._name + "\": " + str(self._quantity)
