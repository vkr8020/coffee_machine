import logging
import time
from collections import OrderedDict
from coffee_machine.core.outlet import Outlet
from coffee_machine.apputils import OutletBusyException

logger = logging.getLogger()


class OutletImpl:
    def __init__(self, num_outlets):
        assert (num_outlets > 0)
        self._num_outlets = num_outlets
        self._outlets = OrderedDict()
        self._setup_outlets()

    @property
    def num_outlets(self):
        return self._num_outlets

    def _setup_outlets(self):
        for i in range(1, self.num_outlets + 1):
            self._outlets[i] = Outlet(i, Outlet.State.FREE)

    def get_free_outlet(self):
        free_outlet = None
        while True:
            try:
                free_outlet = self._check_free_outlet_and_acquire_lock()
                logger.debug("Got a free outlet{0} and acquired the lock".format(free_outlet.id))
                break
            except OutletBusyException as e:
                logger.debug(e)
            time.sleep(1)
            logger.debug("waiting for sometime to re-check for a free outlet ")

        return free_outlet

    def _check_free_outlet_and_acquire_lock(self):
        free_outlet = None
        for outlet in self._outlets.values():
            if outlet.state == Outlet.State.FREE:
                free_outlet = outlet
                break

        if free_outlet is None:
            raise OutletBusyException("All outlets are in processing state. Please wait for some time.")
        else:
            free_outlet.acquire_lock()
            return free_outlet
