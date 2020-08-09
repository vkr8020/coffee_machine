class SeekBeverage:
    def __init__(self, beverage_name):
        assert(beverage_name, str)
        if not beverage_name:
            raise ValueError("beverage name can't be empty")
        self._beverage_name = beverage_name