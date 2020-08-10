import logging
from collections import OrderedDict
from coffee_machine.apputils.exceptions import IngredientUnavailableException, IngredientInsufficientException, IngredientShortageException
logger = logging.getLogger()


class BeverageImpl:
    """
    This class holds teh information about all beverages that the machine can handle
    and a functionality to dispense the requested beverage
    """
    def __init__(self, beverages, ingredient_stock_dict):
        self._beverages_map = OrderedDict()
        self._num_beverages = len(beverages)
        self._init_beverages_map(beverages)
        self._ingredient_stock_dict = ingredient_stock_dict

    def _init_beverages_map(self, beverages):
        for beverage in beverages:
            self._beverages_map[beverage.name] = beverage

    @property
    def num_beverages(self):
        return self._num_beverages

    def dispense_beverage(self, outlet, requested_beverage):
        beverage = self._beverages_map[requested_beverage.name]
        insufficient_ingredients = []
        unavailable_ingredient_flag = 0

        for ingredient in beverage.ingredients:
            # If a particular ingredient is not present in stock , then we can't prepare it.
            if ingredient.name not in self._ingredient_stock_dict:
                ingredient_unavailable_msg = "{0} cannot be prepared because {1} is not available".format(beverage.name, ingredient.name)
                unavailable_ingredient_flag = 1
                break
            stock_ingredient = self._ingredient_stock_dict[ingredient.name]
            # If a particular ingredient is not sufficiently available
            if not stock_ingredient.is_consumable(ingredient.quantity):
                insufficient_ingredients.append(stock_ingredient.name)
                ingredient_insufficient_msg = "{0} cannot be prepared because item {1} is not sufficient".format(beverage.name,  stock_ingredient.name)

        if not insufficient_ingredients and not unavailable_ingredient_flag:
            # all ingredients are available in sufficient quantities
            for ingredient in beverage.ingredients:
                stock_ingredient = self._ingredient_stock_dict[ingredient.name]
                try:
                    stock_ingredient.consume_quantity(ingredient.quantity)
                except IngredientShortageException as e:
                    # this exception is raised when the current quantity of an ingredient in stock is
                    # running low(below the requirement)
                    message = "Ingredient {0} is running low, please refill it".format(ingredient.name)
                    logger.info(message)
            outlet.dispense_beverage(beverage) # dispense the beverage if all requirements are satisfied
        else:
            outlet.release_lock() # release the lock for outlet since the beverage can't be prepared
            if unavailable_ingredient_flag:
                raise IngredientUnavailableException(ingredient_unavailable_msg)
            else:
                raise IngredientInsufficientException(ingredient_insufficient_msg)
