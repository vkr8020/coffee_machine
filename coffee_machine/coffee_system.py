import time
import logging
import threading
from coffee_machine.apputils import BeverageOptionsImpl
from coffee_machine.core.machine_configuration import MachineConfiguration
from coffee_machine.apputils import InvalidInputOptionException, IngredientShortageException, IngredientInsufficientException, IngredientUnavailableException
from coffee_machine.core.outlet_impl import OutletImpl
from coffee_machine.core.beverage_impl import BeverageImpl
from coffee_machine.core.ingredient_impl import IngredientStockImpl
from coffee_machine.core.seek_beverage import SeekBeverage
from coffee_machine.core.utils import read_ingredient_refill_request

logger = logging.getLogger()

class CoffeeMachine:
    def __init__(self, machine_configuration, name="Chai_Point"):
        logger.debug("Setting up "+ name + " machine ")
        self.machine_configuration = machine_configuration
        assert(isinstance(name, str))
        self._name = name

        self._num_threads = self.machine_configuration.outlets
        self._beverage_options_impl = BeverageOptionsImpl(self.machine_configuration.beverages)
        self._beverage_dict = self._beverage_options_impl.get_beverage_dict() # a dict with key as integer and values as Beverage objects
        self._outlet_impl = OutletImpl(self.machine_configuration.outlets)
        self._ingredient_stock_impl = IngredientStockImpl(self.machine_configuration.inventory)
        self._beverage_impl = BeverageImpl(self.machine_configuration.beverages, self._ingredient_stock_impl.get_inventory_ingredient_dict())

    @property
    def name(self):
        return self._name

    def _get_user_beverage_request(self):
        """
        get input from the user , process it and retrun a beverage request accordingly
        :return: beverage request
        """
        while True:
            # display options
            self._beverage_options_impl.display_options()
            try:
                # read an option from stdin
                input_option = self._beverage_options_impl.read_option()
                num_beverages = self._beverage_impl.num_beverages
                if input_option == num_beverages + 1:
                    #refill request
                    refill_ingredient_request = read_ingredient_refill_request(list(self._ingredient_stock_impl.get_inventory_ingredient_dict().keys()))
                    self._ingredient_stock_impl.refill_ingredient_stock(refill_ingredient_request)
                    logger.info("Successfully refilled")
                    logger.debug(self._ingredient_stock_impl.get_inventory_details_msg())
                elif input_option == num_beverages + 2:
                    logger.info(self._ingredient_stock_impl.get_inventory_details_msg())
                else:
                    requested_beverage_name = self._beverage_dict[input_option].name
                    seek_beverage = SeekBeverage(requested_beverage_name)
                    break;
                    #serve beverage
            except InvalidInputOptionException as e:
                print("Please enter a valid option")
        return seek_beverage

    class custom_thread(threading.Thread):
        """
        Custom thread to dispense a beverage through an outlet
        """
        def __init__(self, beverage_impl, free_outlet, requested_beverage):
            threading.Thread.__init__(self)
            self.beverage_impl = beverage_impl
            self.free_outlet = free_outlet
            self.requested_beverage = requested_beverage

        def run(self):
            logger.debug("Inside thread func: Trying to serve {0} on outlet {1}".format(self.requested_beverage.name, self.free_outlet.id))
            try:
                self.beverage_impl.dispense_beverage(self.free_outlet, self.requested_beverage)
            except IngredientUnavailableException as e:
                logger.info(str(e))
            except IngredientInsufficientException as e:
                logger.info(str(e))

    def run(self):
        """
        main logic
        :return:
        """
        while True:
            # Step1: look out for a free outlet
            free_outlet = self._outlet_impl.get_free_outlet()

            # Step2: Get a beverage request from user
            requested_beverage = self._get_user_beverage_request()
            logger.debug("Received a request for {0}".format(requested_beverage.name))
            logger.debug(self._ingredient_stock_impl.get_inventory_details_msg())

            # Step3: Launch a thread to dispense the requested_beverage from the above obtained free_outlet
            cust_thread = self.custom_thread(self._beverage_impl, free_outlet, requested_beverage)
            cust_thread.start()
            try:
                time.sleep(0.5)
            except:
                logger.debug("Error occured when main thread is in sleep mode")