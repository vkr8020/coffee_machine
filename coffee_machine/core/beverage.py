from coffee_machine.core.ingredient import Ingredient


class Beverage:
    _preparation_time: int

    def __init__(self, name, ingredients, preparation_time=10, dispensing_time=3):
        self._name = name
        assert(type(ingredients), list)
        for beverage_ingredient in ingredients:
            if type(beverage_ingredient) is not Ingredient:
                raise TypeError(
                    "Expected beverage ingredient type to be Ingredient but got {0}".format(
                        type(beverage_ingredient)))

        # set the beverage ingredients
        self._ingredients = ingredients
        # preparation time is in ms(milliseconds)
        self._preparation_time = preparation_time
        self._dispensing_time = dispensing_time

    @property
    def __repr__(self):
        ingredients_repr = ''
        for idx, beverage_ingredient in enumerate(self._ingredients):
            ingredients_repr += idx + '.' + beverage_ingredient + '\n'
        return "Name of the beverage is: {n}\nIngredients are:\n" + ingredients_repr

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, s):
        self._name = s

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def preparation_time(self):
        return self._preparation_time

    @property
    def dispensing_time(self):
        return self._dispensing_time
