class SeekBeverage:
    def __init__(self, beverage_name):
        if not beverage_name:
            raise ValueError("beverage name can't be empty")
        self._beverage_name = beverage_name

    @property
    def name(self):
        return self._beverage_name
