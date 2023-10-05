from Unit import Unit
import pandas as pd

class Player:
    
    #Player class constructor
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        self.units = []
    
    #function to determine if a player's units health reach 0, removes unit
    #and indicates unit died if so
    def remove_units(self):
        if len(self.units) > 0:
            for unit in reversed(self.units):
                if unit.health <= 0:
                    print(self.name + "'s " + unit.name + " died!\n")
                    self.units.remove(unit)

    #adjusts all unit base damage depending on tier.
    def adjust_all_damage(self):
        for unit in self.units:
            unit.adjust_damage()

    #merges 3 of the same units into 1 stronger unit. 
    def combine_units(self):
        
        if len(self.units) >= 3:
    
            names = []
            replace = ""

            for unit in self.units:
                names.append(unit.name)

            df = pd.DataFrame(names, columns = ["Names"])
            df = pd.DataFrame(df.groupby(["Names"]).size(), columns = ["Count"])
            df = df[df["Count"] == 3].reset_index()

            if len(df.index) >= 1:
                replace = df.get("Names").iloc[0]

                for unit in self.units:
                    if unit.name == replace:
                        unit.health = 0
                
                self.remove_units()
                
                if "Water" in replace:
                    if "Minion" in replace:
                        self.units.append(Unit(4))
                        print("\n☆☆" + replace + " combined into a " + "Water Guardian!☆☆\n")
                    else:   
                        self.units.append(Unit(8))
                        print("\n☆☆☆" + replace + " combined into a " + "Water King!☆☆☆\n")
                elif "Earth" in replace:
                    if "Minion" in replace:
                        self.units.append(Unit(5))
                        print("\n☆☆" + replace + " combined into a " + "Earth Guardian!☆☆\n")
                    else:   
                        self.units.append(Unit(9))
                        print("\n☆☆☆" + replace + " combined into a " + "Earth King!☆☆☆\n")
                elif "Fire" in replace:
                    if "Minion" in replace:
                        self.units.append(Unit(6))
                        print("\n☆☆" + replace + " combined into a " + "Fire Guardian!☆☆\n")
                    else:   
                        self.units.append(Unit(10))
                        print("\n☆☆☆" + replace + " combined into a " + "Fire King!☆☆☆\n")
                elif "Air" in replace:
                    if "Minion" in replace:
                        self.units.append(Unit(7))
                        print("\n☆☆" + replace + " combined into a " + "Air Guardian!☆☆\n")
                    else:   
                        self.units.append(Unit(11))
                        print("\n☆☆☆" + replace + " combined into a " + "Air King!☆☆☆\n")
                    







