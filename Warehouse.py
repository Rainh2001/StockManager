from Asset import *

class Warehouse(Asset):
    
    count = 0

    def __init__(self, location, inventory=None):
        super().__init__(location, inventory)
        Warehouse.count += 1