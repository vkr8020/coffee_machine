from coffee_machine.core.ingredient import Ingredient
from coffee_machine.core.stock_ingredient import StockIngredient
from coffee_machine.core.beverage import Beverage
from coffee_machine.core.machine_configuration import MachineConfiguration
from coffee_machine.core.utils import read_jsonfile


class ParseJSONConfiguration:
    def __init__(self, data):
        self._process_data(data)

    def _process_data(self, data):
        try:
            self.num_outlets = data['machine']['outlets']['count_n']
        except:
            raise KeyError("number of outlets is not found in the given config data")

        try:
            inv_dict = data['machine']['total_items_quantity']
            self.inventory = []
            for ingredient_name, quantity in inv_dict.items():
                self.inventory.append(StockIngredient(ingredient_name, quantity))
        except:
            raise Exception("Error in reading the total_items_quantity section from json data")

        try:
            beverages_dict = data['machine']['beverages']  # beverages_dict from the json data
            self.beverages = []  # a list of all Beverages
            for beverage_name, ingredients_dict in beverages_dict.items():
                ingredients = []  # a list of all Ingredients
                for ingredient_name, quantity in ingredients_dict.items():
                    ingredients.append(Ingredient(ingredient_name, quantity))
                self.beverages.append(Beverage(beverage_name, ingredients))
        except:
            raise Exception("Error in reading the beverages section from json data")

    @property
    def get_parsed_data(self):
        return self.num_outlets, self.inventory, self.beverages


def get_machine_configuration(inpfile):
    # read the json file
    json_data = read_jsonfile(inpfile)
    # parse the obtained json data and generate machine configuration from it
    num_outlets, inventory, beverages = ParseJSONConfiguration(json_data).get_parsed_data
    machine_config = MachineConfiguration(num_outlets, inventory, beverages)

    return machine_config
