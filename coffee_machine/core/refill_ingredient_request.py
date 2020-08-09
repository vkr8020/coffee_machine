class RefillIngredientRequest:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

