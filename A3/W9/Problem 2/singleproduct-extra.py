class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        if amount >= 100:
            return ((self.price * amount) / 100) * 80
        elif amount >= 10:
            return ((self.price * amount) / 100) * 90
        else:
            return self.price * amount

    def make_purchase(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return True
        return False


if __name__ == "__main__":
    pass
