from coffee_machine.apputils import BeverageOptionsImpl
from coffee_machine.core.machine_configuration import MachineConfiguration
from coffee_machine.apputils import InvalidInputOptionException


class CoffeeMachine:
    def __init__(self, machine_configuration, name="Chai_Point"):
        assert(isinstance(machine_configuration, MachineConfiguration))
        self.machine_configuration = machine_configuration
        assert(isinstance(name, str))
        self._name = name
        self._beverage_options_impl = BeverageOptionsImpl(self.machine_configuration.beverages)


    @property
    def name(self):
        return self._name

    def get_user_beverage_request(self):
        while(True):
            # display options
            self._beverage_options_impl.display_options()
            try:
                # read an option from stdin
                input_option = self._beverage_options_impl.read_option()
                if input_option == 0:
                    #refill request
                    print("Refill Request")
                else:
                    print("Serve beverage request")
                    #serve beverage
            except InvalidInputOptionException as e:
                print("Please enter a valid option")


    def run(self):
        while(True):
            # Step1: look out for a free outlet
            # Step2: Get a beverage request from user
            # if received a valid request then, execute a thread to either refill the beverage or dispense the beverage
            # otherwise, may be invalid option: So display options again to choose a valid one
            #
            break

        self.get_user_beverage_request()




