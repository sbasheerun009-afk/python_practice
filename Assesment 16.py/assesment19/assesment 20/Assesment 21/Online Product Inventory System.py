class Private:
    def __init__(self,name,prices):
        self.__product_name = name
        self.__prices = prices
    def get_name(self):
        return self.__product_name
    def get_prices(self):
        return self.__prices
class InventoryManagement(Private):
    def get_min_price(self):
        return min(self.get_prices())
    def get_max_price(self):
        return max(self.get_prices())
    def Expensivecount(self):
        count = 0
        for p in self.get_prices():
            if p >= 1000:
                count += 1
        return count
    def upper_name(self):
        return self.get_name().upper()
    def is_palindrome(self):
        name = self.get_name().lower()
        return name == name[::-1]
product_name = input()
n = int(input())
prices = list(map(int,input().split()))
product =InventoryManagement(product_name,prices)
print(f"productname:{product.get_name()}")
print(f"uppercase:{product.upper_name()}")
print(f"minimumprice:{product.get_min_price()}")
print(f"maximumprice:{product.get_max_price()}")
print(f"expensivecount:{product.Expensivecount()}")
print(f"is_palindrome:{product.is_palindrome()}")




