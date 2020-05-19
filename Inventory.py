class Inventory:

    def __init__(self, itemDictionary):
        self.items = itemDictionary

    def itemQuantity(self, itemId):
        if(self.items[itemId] == None):
            return None
        
        return self.items[itemId].quantity

    def addQuantity(self, itemId, quantity=1):
        pass

    def removeQuantity(self, itemId, quantity=1):
        self.items[itemId].quantity -= quantity
        return self.items[itemId].quantity

    def removeAllQuantity(self, itemId):
        self.items[itemId].quantity = 0
        return 0

    def addItem(self, product, quantity):
        self.items[product.id] = {
            "product" : product,
            "quantity" : quantity
        }
