class Ingredient:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    def __str__(self):
        # TODO CHECK
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def __repr__(self):
        return "\"" + self._name + "\": " + str(self._quantity)
