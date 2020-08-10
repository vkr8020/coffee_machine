from collections import OrderedDict


class IngredientStockImpl:
    """
    A class which holds the information about inventory stock.
    This supports refilling an ingredient stock, get inventory details.
    """
    def __init__(self, inventory):
        self._ingredient_stock_dict = OrderedDict()
        self._init_ingredient_stock_dict(inventory)

    def _init_ingredient_stock_dict(self, inventory):
        """
        initialize the ingredient_stock_dict where key is a ingredient name and value is an Ingredient object
        :param inventory: a list of ingredients
        :return:

        """
        for stock_ingredient in inventory:
            self._ingredient_stock_dict[stock_ingredient.name] = stock_ingredient

    def get_inventory_ingredient_dict(self):
        return self._ingredient_stock_dict

    def get_inventory_details_msg(self):
        """
        :return: full inventory details
        """
        msg = "Current Items in Inventory are:\n"
        for stock_ingredient in self._ingredient_stock_dict.values():
            msg += str(stock_ingredient) + '\n'

        return msg

    def refill_ingredient_stock(self, refill_ingredient_request):
        """
        Assuming that only the item names that are already existing in the inventory (i.e stock ingredient names mentioned in the json file) can be refilled.
        :param refill_ingredient_request:
        :return:
        """
        if refill_ingredient_request.name not in self._ingredient_stock_dict:
            raise KeyError("Ingredient {0} for refilling doesn\'t exist in the inventory".format(refill_ingredient_request.name))
        ingredient_stock = self._ingredient_stock_dict[refill_ingredient_request.name]
        ingredient_stock.add_quantity(refill_ingredient_request.quantity)
