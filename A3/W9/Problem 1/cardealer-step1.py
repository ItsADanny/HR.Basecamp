class Car:
    # Default values for all cars
    sold = False

    # This will called when
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def sell(self):
        self.sold = True

    def print(self):
        str_sold = ""
        if self.sold:
            str_sold = "Sold"
        else:
            str_sold = "Not sold yet"

        print(f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nPrice: {self.price}\n{str_sold}")
