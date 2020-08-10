from coffee_machine.core.ingredient import Ingredient
from coffee_machine.core.stock_ingredient import StockIngredient
from coffee_machine.core.beverage import Beverage


class MachineConfiguration:
    #_outlets: int

    def __init__(self, outlets, inventory, beverages):
        """
        This class has all the information about the machine
        outlets: number of outlets that are present in the machine
        inventory: list of all ingredients
        beverages: list of all beverages that the machine can prepare
        """
        assert (isinstance(outlets, int))
        assert (outlets > 0)
        self._outlets = outlets

        # Assuming that this machine will have an inventory of only Ingredients
        for inv_item in inventory:
            if type(inv_item) is not StockIngredient:
                raise TypeError(
                    "Expected beverage ingredient type to be StockIngredient but got {0}".format(
                        type(inv_item)))
        self._inventory = inventory

        for beverage_item in beverages:
            if type(beverage_item) is not Beverage:
                raise TypeError(
                    "Expected beverage item type to be Beverage but got {0}".format(
                        type(beverage_item)))
        self._beverages = beverages

    @property
    def outlets(self):
        return self._outlets

    @property
    def inventory(self):
        return self._inventory

    @property
    def beverages(self):
        return self._beverages
