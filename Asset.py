class Asset:

    count = 0

    def __init__(self, location, inventory=None):
        self.location = location
        self.inventory = inventory
        Asset.count += 1

    # def addInventory(self, inventory):
    #     self.inventory.append(inventory)
    #     return inventory

    # def removeInventory(self, inventoryId):
    #     for i in range(len(self.inventory)):
    #         if self.inventory[i].id == inventoryId:
    #             return self.inventory.pop(i)
    #     return None
    