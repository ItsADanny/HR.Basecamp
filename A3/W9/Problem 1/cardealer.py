class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Name: {self.name}")


class Car:
    # Default values for all cars
    sold = False
    sold_to = None

    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def sell(self, customer: Customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        if self.sold:
            print(f"Brand: {self.brand}\nModel: {self.model}"
                  f"Color: {self.color}\nPrice: {self.price}\nSold to: {self.sold_to.name}")
        else:
            print(f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nPrice: {self.price}")


class Motorcycle:
    # Default values for all Motorcycles
    sold = False
    sold_to = None

    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def sell(self, customer: Customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        if self.sold:
            print(f"Brand: {self.brand}\nModel: {self.model}"
                  f"Color: {self.color}\nPrice: {self.price}\nSold to: {self.sold_to.name}")
        else:
            print(f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nPrice: {self.price}")


if __name__ == "__main__":
    pass
