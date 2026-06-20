class InvalidProductIndexError(Exception):
    pass


class OutOfStockError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class EmptyInventoryError(Exception):
    pass


class Inventory:
    def __init__(self, products):
        self.products = products

    def purchase(self, index, quantity):

        if not self.products:
            raise EmptyInventoryError("Inventory is empty.")

        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0.")

        if index < 0 or index >= len(self.products):
            raise InvalidProductIndexError("Invalid product index.")

        if quantity > self.products[index]:
            raise OutOfStockError("Requested quantity exceeds available stock.")

        self.products[index] -= quantity

        print("Remaining stock:", self.products[index])


try:
    n = int(input())

    products = list(map(int, input().split()))

    index = int(input())

    quantity = int(input())

    inventory = Inventory(products)

    inventory.purchase(index, quantity)

except InvalidProductIndexError as e:
    print(f"InvalidProductIndexError: {e}")

except OutOfStockError as e:
    print(f"OutOfStockError: {e}")

except InvalidQuantityError as e:
    print(f"InvalidQuantityError: {e}")

except EmptyInventoryError as e:
    print(f"EmptyInventoryError: {e}")