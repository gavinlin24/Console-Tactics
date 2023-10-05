import random

class Unit:

    #Unit class constructor, sets tier, name, and health based on type.
    def __init__(self, type):
        self.name = ""
        self.cost = 3
        self.base_damage = 0
        self.true_damage = 0
        self.health = 1
        self.type = type
        self.tier = 0

        if self.type <= 3:

            self.health = 3

            if self.type == 0:
                self.name = "Water Minion"
                self.tier = 1
            elif self.type == 1:
                self.name = "Earth Minion"
                self.tier = 1
            elif self.type == 2:
                self.name = "Fire Minion"
                self.tier = 1
            else:
                self.name = "Air Minion"
                self.tier = 1

        elif self.type <= 7:

            self.health = 6

            if self.type == 4:
                self.name = "Water Guardian"
                self.tier = 2
            elif self.type == 5:
                self.name = "Earth Guardian"
                self.tier = 2
            elif self.type == 6:
                self.name = "Fire Guardian"
                self.tier = 2
            else:
                self.name = "Air Guardian"
                self.tier = 2
        else:

            self.health = 9
            
            if self.type == 8:
                self.name = "Water King"
                self.tier = 3
            elif self.type == 9:
                self.name = "Earth King"
                self.tier = 3
            elif self.type == 10:
                self.name = "Fire King"
                self.tier = 3
            else:
                self.name = "Air King"
                self.tier = 3

    #adjusts base damage to a random number in a range depending on Unit tier
    def adjust_damage(self):
        if self.tier == 1:
            self.base_damage = random.randint(0,1)
        elif self.tier == 2:
            self.base_damage = random.randint(0,3)
        else:
            self.base_damage = random.randint(0,5)


