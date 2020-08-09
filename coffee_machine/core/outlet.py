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

    @state.setter
    def state(self, s):
        self._state = s

    def dispense_beverage(self, beverage):
        assert(type(beverage), Beverage)
        print(beverage.name + "is being prepared. Dispensing on Outlet:{0}".format(self.id) + ".....")
        time.sleep(beverage.preparation_time) # set for 1000ms
        print("Success: Dispensed {0} on Outlet {1}".format(beverage.name, self.id))

    def acquire_lock(self):
        if self.state == self.State.FREE:
            self.state(self.State.RUNNING)
        else:
            raise OutletBusyException("Error: Trying to acquire a lock for outlet which is busy")

    def release_lock(self):
        if self.state == self.State.RUNNING:
            self.state(self.state.FREE)