#   This is a Python script to calculate the results of a risk battle
#
#   Copyright (C) 2015 by Joshua Rystedt
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   To read a copy of the GNU General Public License see <http://www.gnu.org/licenses/>.

# Imports
from random import randint, choice
from termcolor import cprint
from sys import exit

# The Attacker's number of dice
def calc_attack_dice(armies):
    if armies >= 3:
        attack_dice = 3
        return attack_dice
    elif armies == 2:
        attack_dice = 2
        return attack_dice
    elif armies == 1:
        attack_dice = 1
        return attack_dice

# The Defender's number of dice
def calc_defence_dice(armies):
    if armies >= 2:
        defence_dice = 2
        return defence_dice
    elif armies == 1:
        defence_dice = 1
        return defence_dice

# Roll the Attacker's dice
def attacker_rolls(attack_dice):
    attacker_roll_result = []
    if attack_dice >= 3:
        attacker_roll_result += [randint(1,6), randint(1,6), randint(1,6)]
    elif attack_dice == 2:
        attacker_roll_result += [randint(1,6), randint(1,6)]
    elif attack_dice == 1:
        attacker_roll_result = [randint(1,6)]
    attacker_roll_result.sort(reverse=True)
    print "The attacker rolled: " + str(attacker_roll_result)
    return attacker_roll_result

# Roll the Defender's dice
def defender_rolls(defence_dice):
    defender_roll_result = []
    if defence_dice >= 2:
        defender_roll_result += [randint(1,6), randint(1,6)]
    elif defence_dice == 1:
        defender_roll_result += [randint(1,6)]
    defender_roll_result.sort(reverse=True)
    print "The defender rolled: " + str(defender_roll_result)
    print
    return defender_roll_result

# Calculate attacker casualties
def calc_att_casual (attacker_armies, defender_armies, attacker_roll_result, defender_roll_result):

    attacker_loses = 0
    defender_loses = 0

    if attacker_roll_result[0] > defender_roll_result[0]:
        defender_loses += 1
    elif defender_roll_result[0] >= attacker_roll_result[0]:
        attacker_loses += 1

    if len(attacker_roll_result) >= 2 and len(defender_roll_result) >= 2:
        if attacker_roll_result[1] > defender_roll_result[1]:
            defender_loses  += 1
        elif defender_roll_result[1] >= attacker_roll_result[1]:
            attacker_loses += 1

    if attacker_loses == 1:
        lossstring = "army"
    else:
        lossstring = "armies"

    print "The attacker loses " + str(attacker_loses) + " " + lossstring

    attacker_armies -= attacker_loses
    defender_armies -= defender_loses

    if attacker_armies == 1:
        armystring = "army"
    else:
        armystring = "armies"

    print "The attacker has " + str(attacker_armies) + " " + armystring + " remaining"
    print

    return attacker_armies

# Calculate defender casualties
def calc_def_casual (attacker_armies, defender_armies, attacker_roll_result, defender_roll_result):

    attacker_loses = 0
    defender_loses = 0

    if attacker_roll_result[0] > defender_roll_result[0]:
        defender_loses += 1
    elif defender_roll_result[0] >= attacker_roll_result[0]:
        attacker_loses += 1

    if len(attacker_roll_result) >= 2 and len(defender_roll_result) >= 2:
        if attacker_roll_result[1] > defender_roll_result[1]:
            defender_loses  += 1
        elif defender_roll_result[1] >= attacker_roll_result[1]:
            attacker_loses += 1

    if defender_loses == 1:
        lossstring = "army"
    else:
        lossstring = "armies"

    print "The defender loses " + str(defender_loses) + " " + lossstring

    attacker_armies -= attacker_loses
    defender_armies -= defender_loses

    if defender_armies == 1:
        armystring = "army"
    else:
        armystring = "armies"

    print "The defender has " + str(defender_armies) + " " + armystring + " remaining"

    return defender_armies

def victory(attacker_armies, defender_armies):
    if attacker_armies == 0:
        if defender_armies == 1:
            defarmystring = "army"
        else:
            defarmystring = "armies"
        cprint("The defender wins!", "blue", attrs=["bold"])
        cprint("* With " + str(defender_armies) + " " + defarmystring + " remaining", "blue", attrs=["bold"])
        print
        print "----------------------------"
        print
        exit(0)
    elif defender_armies == 0:
        if attacker_armies == 1:
            attarmystring = "army"
        else:
            attarmystring = "armies"
        cprint("The attacker wins!", "red", attrs=["bold"])
        cprint("* With " + str(attacker_armies) + " " + attarmystring + " remaining", "red", attrs=["bold"])
        print
        print "----------------------------"
        print
        exit(0)
    else:
        if defender_armies == 1:
            defarmystring = "army"
        else:
            defarmystring = "armies"
        if attacker_armies == 1:
            attarmystring = "army"
        else:
            attarmystring = "armies"
        cprint("The defender wins!", "blue", attrs=["bold"])
        cprint("* With " + str(defender_armies) + " " + defarmystring + " remaining", "blue", attrs=["bold"])
        print
        cprint("The attacker retreated...", "red", attrs=["bold"])
        cprint("* With " + str(attacker_armies) + " " + attarmystring + " remaining", "red", attrs=["bold"])
        print
        print "----------------------------"
        print
        exit(0)

# Give the attacker the option to retreat when battle is no longer in his favor
def retreatOption(attacker_armies, defender_armies):
    retreatResponses = ["Attacker, would you like to retreat? ",
                        "Attacker, your armies are being annihilated! Would you like to retreat? ",
                        "Attacker, things are looking bleak... Would you like to retreat? ",
                        "Attacker, don't push your luck. Would you like to retreat? ",
                        "Attacker, you are losing! Want to retreat? "]

    if attacker_armies == 1:
        attArmyString = "army"
    else:
        attArmyString = "armies"

    if defender_armies == 1:
        defArmyString = "army"
    else:
        defArmyString = "armies"

    if attacker_armies <= defender_armies:
        print
        userIntention = raw_input(choice(retreatResponses))
        userIntention = userIntention.lower()
        if "y" in userIntention:
            retreat = True
            return retreat
        elif "n" in userIntention:
            retreat = False
            return retreat
        else:
            print "Error! Please enter either yes or no."
            retreat = "Error"
            return retreat
    else:
        retreat = False
        return retreat

def retreatActual(attacker_armies, defender_armies):
    retreat = retreatOption(attacker_armies, defender_armies)
    if retreat == True:
        print
        print "----------------------------"
        print
        victory(attacker_armies,defender_armies)
    elif retreat == False:
        pass
    elif retreat == "Error":
        retreatActual(attacker_armies,defender_armies)
    else:
        print "An unexpected error occurred"
        exit(1)
    print
    print "----------------------------"
    print

# Run RiskRoller
def roll():
    print
    attacker_armies = int(raw_input("How many armies are attacking? "))
    defender_armies = int(raw_input("How many armies are defending? "))
    print
    print "----------------------------"
    print
    while attacker_armies > 0 and defender_armies > 0:
        attacker_roll_result = attacker_rolls(calc_attack_dice(attacker_armies))
        defender_roll_result = defender_rolls(calc_defence_dice(defender_armies))
        attacker_armies = calc_att_casual(attacker_armies,
                    defender_armies,
                    attacker_roll_result,
                    defender_roll_result)
        defender_armies = calc_def_casual(attacker_armies,
                    defender_armies,
                    attacker_roll_result,
                    defender_roll_result)
        retreatActual(attacker_armies, defender_armies)
    else:
        victory(attacker_armies, defender_armies)

# Execute
roll()