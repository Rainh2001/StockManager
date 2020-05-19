from Asset import *

class Shop(Asset):
    
    count = 0

    def __init__(self, location, inventory=None):
        super().__init__(location, inventory)
        Shop.count += 1
