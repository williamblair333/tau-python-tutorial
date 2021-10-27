#################################################################################
'''Multiple Inheritance example WITHOUT super
Here's some super articles though - you need to learn this
https://blog.finxter.com/python-super-function/
https://www.programiz.com/python-programming/methods/built-in/super
https://realpython.com/python-super/
https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
'''

#parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

#parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment in in section {}, {}.".format(self.section, self.type))

class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirts(self):
        print("{} {} on sale".format(self.color, self.name))

Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirts()