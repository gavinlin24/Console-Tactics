from Player import Player
from Shop import Shop
import random
import math

#Main class that handles all game logic.

#prompts player names
player_one_name = input("Player 1 Name: \n")
print("\n")
player_two_name = input("Player 2 Name: \n")

print("\n")

player_one = Player(player_one_name)
player_two = Player(player_two_name)

shop = Shop()

phase = 0
run = True

#sets units true damage to 2X base damage if opposing unit is weak to unit type
def adjust_true_damage(unit_one, unit_two):
    if "Water" in unit_one.name:
        if "Fire" in unit_two.name:
            unit_one.true_damage = unit_one.base_damage * 2
        else:
            unit_one.true_damage = unit_one.base_damage
    elif "Earth" in unit_one.name:
        if "Water" in unit_two.name:
            unit_one.true_damage = unit_one.base_damage * 2
        else:
            unit_one.true_damage = unit_one.base_damage
    elif "Fire" in unit_one.name:
        if "Air" in unit_two.name:
            unit_one.true_damage = unit_one.base_damage * 2
        else:
            unit_one.true_damage = unit_one.base_damage
    else:
        if "Earth" in unit_two.name:
           unit_one.true_damage = unit_one.base_damage * 2
        else:
            unit_one.true_damage = unit_one.base_damage

#function where players' units are randomly selected to battle each other
#if both players have no units, both take 5 damage
#players lose health if a unit that is receiving an attack reaches negative (ex. unit -2 health, player loses 2 hp)
#if one player has more units than the other, units not selected to battle another unit attack the player
def battle(player_one, player_two):

    if len(player_one.units) == len(player_two.units):

        if len(player_one.units) == 0 and len(player_two.units) == 0:
            player_one.health -= 5
            player_two.health -= 5
            print("Both " + player_one_name + " and " + player_two_name + " lost 5 health without the protection" +
                  " of their units!")
            print(player_one_name + " now has " + str(player_one.health) + " health!")
            print(player_two_name + " now has " + str(player_two.health) + " health!")

            
        else:
            player_one_units = random.sample(player_one.units, len(player_two.units))

            for i in range(len(player_two.units)):
                adjust_true_damage(player_two.units[i], player_one_units[i])
                difference = player_one_units[i].health - player_two.units[i].true_damage
                player_one_units[i].health -= player_two.units[i].true_damage
                print(player_two_name + "'s " + player_two.units[i].name + " dealt " + str(player_two.units[i].true_damage) + 
                    " damage to " + player_one_name + "'s " + player_one_units[i].name)
                if difference < 0:
                    print(player_one_name + " took " + str(math.abs(difference)) + " damage! (" + str(player_one.health) + " health remaining)")
                    player_one.health += difference

            for i in range(len(player_two.units)):
                adjust_true_damage(player_one_units[i], player_two.units[i])
                difference = player_two.units[i].health - player_one_units[i].true_damage
                player_two.units[i].health -= player_one_units[i].true_damage
                print(player_one_name + "'s " + player_one_units[i].name + " dealt " + str(player_one_units[i].true_damage) + 
                    " damage to " + player_two_name + "'s " + player_two.units[i].name)
                if difference < 0:
                    print(player_two_name + " took " + str(math.abs(difference)) + " damage! (" + str(player_two.health) + " health remaining)")
                    player_two.health += difference

    elif len(player_one.units) > len(player_two.units):
            
        player_one_units = random.sample(player_one.units, len(player_two.units))
        remaining_units = [unit for unit in player_one.units if unit not in player_one_units]

        for i in range(len(player_two.units)):
            adjust_true_damage(player_two.units[i], player_one_units[i])
            difference = player_one_units[i].health - player_two.units[i].true_damage
            player_one_units[i].health -= player_two.units[i].true_damage
            print(player_two_name + "'s " + player_two.units[i].name + " dealt " + str(player_two.units[i].true_damage) + 
                  " damage to " + player_one_name + "'s " + player_one_units[i].name)
            if difference < 0:
                player_one.health += difference
                print(player_one_name + " took " + str(math.abs(difference)) + " damage! (" + str(player_one.health) + " health remaining)")

        for i in range(len(player_two.units)):
            adjust_true_damage(player_one_units[i], player_two.units[i])
            difference = player_two.units[i].health - player_one_units[i].true_damage
            player_two.units[i].health -= player_one_units[i].true_damage
            print(player_one_name + "'s " + player_one_units[i].name + " dealt " + str(player_one_units[i].true_damage) + 
                  " damage to " + player_two_name + "'s " + player_two.units[i].name)
            if difference < 0:
                player_two.health += difference
                print(player_two_name + " took " + str(math.abs(difference)) + " damage! (" + str(player_two.health) + " health remaining)")
            
        for unit in remaining_units:
            player_two.health -= unit.base_damage
            print(player_two_name + " took " + str(unit.base_damage) + " from " + unit.name + "! (" + str(player_two.health) + " health remaining)")
        
    else:

        player_two_units = random.sample(player_two.units, len(player_one.units))
        remaining_units = [unit for unit in player_two.units if unit not in player_two_units]

        for i in range(len(player_one.units)):
            adjust_true_damage(player_two_units[i], player_one.units[i])
            difference = player_one.units[i].health - player_two_units[i].true_damage
            player_one.units[i].health -= player_two_units[i].true_damage
            print(player_two_name + "'s " + player_two_units[i].name + " dealt " + str(player_two_units[i].true_damage) + 
                  " damage to " + player_one_name + "'s " + player_one.units[i].name)
            if difference < 0:
                player_one.health += difference
                print(player_one_name + " took " + str(math.abs(difference)) + " damage! (" + str(player_one.health) + " health remaining)")

        for i in range(len(player_one.units)):
            adjust_true_damage(player_one.units[i], player_two_units[i])
            difference = player_two_units[i].health - player_one.units[i].true_damage
            player_two_units[i].health -= player_one.units[i].true_damage
            print(player_one_name + "'s " + player_one.units[i].name + " dealt " + str(player_one.units[i].true_damage) + 
                  " damage to " + player_two_name + "'s " + player_two_units[i].name)
            if difference < 0:
                player_two.health += difference
                print(player_two_name + " took " + str(math.abs(difference)) + " damage! (" + str(player_two.health) + " health remaining)")
        
        for unit in remaining_units:
            player_one.health -= unit.base_damage
            print(player_one_name + " took " + str(unit.base_damage) + " from " + unit.name + "! (" + str(player_one.health) + " health remaining)")

#function that displays all of a player's units
def print_minions(player):
    names = []

    for unit in player.units:
        names.append(unit.name)

    print("\n" + player.name + "'s Units: ")
    print(names)
    print("\n")


#main game loop
while run:

    #ends game loop if either player health reaches 0
    #prints out the winner
    if player_one.health == 0 or player_two.health == 0:
        if player_one.health > 0:
            print("\n♕"+player_one_name + " wins!♕")
        elif player_two.health > 0:
            print("\n♕"+player_two_name + " wins!♕")
        else:
            print("TIE GAME!")
        
        run = False

    #gives each player 3 gold at the start of each round
    if phase == 0:
        player_one.gold += 3
        player_two.gold += 3
        phase += 1
    
    #player 1 turn
    if phase == 1:
        if player_one.gold < 3:
            print("No more gold!\n")
            phase += 1
        elif len(player_one.units) == 5:
            print("You have the maximum amount of Units!\n")
            phase += 1
        else:
            print("\n<<<" + player_one_name + "'s turn!" + ">>>\n")
            print("Gold: ")
            print(player_one.gold)
            shop.refresh()
            shop.display()
            print_minions(player_one)
            selection = input("Type a number to buy or skip: ")
            selection = int(selection)
            print("\n")

            if selection == 4:
                phase += 1
            else:
                player_one.units.append(shop.units[selection - 1])
                player_one.gold -= 3
                print(player_one_name + " purchased a " + shop.units[selection - 1].name + "!\n")
                player_one.combine_units()
                player_one.adjust_all_damage()
    
    #player 2 turn
    if phase == 2:
        if player_two.gold < 3:
            print("No more gold!\n")
            phase += 1
        elif len(player_two.units) == 5:
            print("You have the maximum amount of Units!\n")
            phase += 1
        else:
            print("\n<<<" + player_two_name +"'s turn!" + ">>>\n")
            print("Gold: ")
            print(player_two.gold)
            shop.refresh()
            shop.display()
            print_minions(player_two)
            selection = input("Type a number to buy or skip: ")
            selection = int(selection)
            print("\n")

            if selection == 4:
                phase += 1
            else:
                player_two.units.append(shop.units[selection - 1])
                player_two.gold -= 3
                print(player_two_name + " purchased a " + shop.units[selection - 1].name + "!\n")
                player_two.combine_units()
                player_two.adjust_all_damage()

    #battle phase
    if phase == 3:

        battle(player_one, player_two)
        player_one.remove_units()
        player_two.remove_units()

        phase = 0




