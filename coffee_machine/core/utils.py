import os
import json
from coffee_machine.apputils.exceptions import FileHandlingException, InvalidInputOptionException
from coffee_machine.core.refill_ingredient_request import RefillIngredientRequest


def read_jsonfile(inpfile):
    """
    :param inpfile: and input json file
    :return: json data in dict format
    """
    if not os.path.exists(inpfile):
        raise FileNotFoundError("Couldn\'t find the {0} file".format(inpfile))
    try:
        with open(inpfile) as f:
            json_data = json.load(f)
    except:
        raise FileHandlingException("Couldn\'t read the json file[{0}]".format(inpfile))

    return json_data


def read_ingredient_refill_request(stock_ingredients):
    """
    :param stock_ingredients: a list of inventory ingredients name
    :return: refill ingredient request
    """
    display_data = ''
    for idx, ingredient_name in enumerate(stock_ingredients):
        display_data += str(idx + 1) + '.' + ingredient_name + '\n'

    print(display_data)

    def read_data(stock_ingredients):
        while True:
            print("Please specify the ingredient option number to refill")
            try:
                input_option = int(input())
                assert (1 <= input_option <= len(stock_ingredients))
                while True:
                    print("Please enter the quantity(in ml) to refill")
                    try:
                        quantity = int(input())
                        assert (quantity > 0)
                        break
                    except:
                        print("Please enter the appropriate quantity")
                break
            except:
                raise InvalidInputOptionException("Please specify a valid input option")

        return RefillIngredientRequest(stock_ingredients[input_option - 1], quantity)

    while True:
        try:
            refill_ingredient_request = read_data(stock_ingredients)
            break
        except InvalidInputOptionException as e:
            print(e)

    return refill_ingredient_request
