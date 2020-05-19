class Product:

    def __init__(self, identifier, name, cost, category=None):
        self.id = identifier
        self.name = name
        self.cost = cost
        self.category = category

    def addSupplier(self):
        pass

    def removeSupplier(self):
        pass