import random
from Unit import Unit

class Shop:

    #Constructor for Shop class
    def __init__(self):
        self.units = []
    
    #Creates 4 random units in a player shop
    def refresh(self):

        self.units.clear()

        slot_one = random.randint(0,3)
        slot_two = random.randint(0,3)
        slot_three = random.randint(0,3)

        self.units.append(Unit(slot_one))
        self.units.append(Unit(slot_two))
        self.units.append(Unit(slot_three))
    
    #Displays all units in shop
    def display(self):

        print("\n***UNIT SHOP***\n")

        for unit in self.units:
            print(self.units.index(unit) + 1, end=" ")
            print(" ", unit.name)

        print("4   Skip")
        print("\n****************")


        