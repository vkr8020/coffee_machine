import time
from enum import Enum
from coffee_machine.apputils.exceptions import OutletBusyException
from coffee_machine.core.beverage import Beverage


class Outlet:
    class State(Enum):
        FREE = 0
        RUNNING = 1
        ERROR = 2

    def __init__(self, id, state=State.FREE):
        """
        :type id: int
        :type state: State
        """
        self._id = id
        self._state = state

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    def set_state(self, s):
        self._state = s

    def dispense_beverage(self, beverage):
        print(beverage.name + " is being prepared and will be dispensed at Outlet:{0}".format(self.id))
        time.sleep(beverage.preparation_time) # set for 7sec by default
        print("Success: {0} is prepared and dispensing on Outlet {1} ...".format(beverage.name, self.id))
        time.sleep(beverage.dispensing_time) # set to 3 sec by default
        self.release_lock()

    def acquire_lock(self):
        if self.state == self.State.FREE:
            self.set_state(self.State.RUNNING)
        else:
            raise OutletBusyException("Error: Trying to acquire a lock for outlet which is busy")

    def release_lock(self):
        if self.state == self.State.RUNNING:
            self.set_state(self.state.FREE)