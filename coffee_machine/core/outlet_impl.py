from collections import OrderedDict
from coffee_machine.core.outlet import Outlet


class OutletImpl:
    def __init__(self, num_outlets):
        assert (num_outlets > 0)
        self._num_outlets = num_outlets

    @property
    def num_outlets(self):
        return self._num_outlets

    def setup_outlets(self):
        self._outlets = OrderedDict()
        for i in range(1, self.num_outlets+1):
            self._outlets[i] = Outlet(i, Outlet.State.FREE)

    def get_free_outlet(self):
        pass