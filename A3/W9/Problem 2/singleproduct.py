class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        return self.price * amount

    def make_purchase(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return True
        return False
