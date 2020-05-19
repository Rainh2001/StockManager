from Location import *
from Asset import *
from Warehouse import *
from Shop import *

class StockManager:
    @staticmethod
    def main():
        print("StockManager")

        wh1 = Warehouse(Location("Ashbury", (-33, -44)))
        wh2 = Warehouse(Location("Newcastle", (-33, -40)))

        shop1 = Shop(Location("Sydney", (-33, -44)))
        shop2 = Shop(Location("Melbourne", (-33, -50)))

    

if __name__ == "__main__":
    StockManager.main()
