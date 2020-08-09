from coffee_machine.core.beverage import Beverage
from coffee_machine.apputils.exceptions import InvalidInputOptionException


class BeverageOptionsImpl:
    def __init__(self, beverages):
        assert (isinstance(beverages, list))
        for beverage in beverages:
            assert (isinstance(beverage, Beverage))
        self._beverages = beverages

    def display_options(self):
        display_data = '0.Refill\n'
        for idx, beverage in enumerate(self._beverages):
            display_data += str(idx+1) + '.' + beverage.name + '\n'
        print("Dispenser is ready to serve. Please enter an option number")
        print(display_data)

    def read_option(self):
        print(">>>", end='')
        try:
            input_option = int(input())
            assert (0 <= input_option <= len(self._beverages))
        except:
            raise InvalidInputOptionException

        return input_option
