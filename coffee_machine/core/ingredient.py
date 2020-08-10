class Ingredient:
    """
    A class for Ingredient item
    """
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def __repr__(self):
        return "\"" + self._name + "\": " + str(self._quantity)

    def __str__(self):
        return "\"" + self._name + "\": " + str(self._quantity)