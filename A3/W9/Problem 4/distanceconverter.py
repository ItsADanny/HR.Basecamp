class Converter:

    def __init__(self, length, unit):
        if unit == "inches":
            length = length / 39.37
            self.length = length
            self.unit = unit
        elif unit == "feet":
            length = length / 3.280839895
            self.length = length
            self.unit = unit
        elif unit == "yards":
            length = length / 1.0936132983
            self.length = length
            self.unit = unit
        elif unit == "miles":
            length = length * 1609.344
            self.length = length
            self.unit = unit
        elif unit == "meters":
            self.length = length
            self.unit = unit
        elif unit == "kilometers":
            length = length * 1000
            self.length = length
            self.unit = unit
        elif unit == "centimeters":
            length = length / 100
            self.length = length
            self.unit = unit
        elif unit == "millimeters":
            length = length / 1000
            self.length = length
            self.unit = unit
        else:
            raise ValueError("TEST")

    def inches(self):
        return self.length * 39.37

    def feet(self):
        return self.length * 3.280839895

    def yards(self):
        return self.length * 1.0936132983

    def miles(self):
        return self.length / 1609.344

    def kilometers(self):
        return self.length / 1000

    def meters(self):
        return self.length

    def centimeters(self):
        return self.length * 100

    def millimeters(self):
        return self.length * 1000
