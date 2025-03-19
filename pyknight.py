import random
#[0]N/A [1]Player Name [2]LVL [3]EXP [4]EXPM [5]GLD [6]HP [7]HPM [8]DEF [9]ATT [10]MATT [11]MAN [12]MANM [13]SPD
playerstts = ["N/A", "Default", 1, 0, 25, 5, 20, 20, 0, 3, 0, 2, 2, 3]
#[0]N/A [1]Weapon Name [2]ATT [3]MATT [4]BPrice [5]SPrice [6]Owned
playerwpn = ["N/A", "Stick", 2, 0, 1, 1, 1,
"Iron Shortsword", 4, 0, 50, 25, 0,
"Iron Longsword", 7, 0, 175, 75, 0,
"Iron Claymore", 13, 0, 835, 200, 0,
"Steel Longsword", 15, 0, 1225, 600, 0,
"Steel Claymore", 23, 0, 2925, 1400, 0,
"Tome of Magic", 1, 5, 175, 50, 0,
"Sapphire Staff", 3, 9, 1575, 700, 0,
"Ruby Staff", 4, 15, 2550, 1200, 0,
"Dragonfire Staff", 5, 22, 5675, 2500, 0]
#[0]N/A [1]Armour Name [2]DEF [3]RunAdd [4]BPrice [5]SPrice [6]Owned
playeramr = ["N/A", "Cloth Tunic", 0, 3, 2, 1, 1,
"Leather Armor", 2, 1, 80, 50, 0,
"Brass Armor", 3, -2, 475, 200, 0,
"Iron Armor", 4, -3, 900, 400, 0,
"Steel Armor", 6, -7, 5275, 2000, 0,
"Dragon Scale Armor", 8, -6, 10000, 4000, 0]
#[0]N/A [1]Consumable [2]SA1 [3]B/D1 [4]SA2 [5]B/D2 [6]SA3 [7]B/D3 [8]BPrice [9]SPrice [10]Owned
consumables = ["N/A", "Bread", 6, 7, 0, 0, 0, 0, 3, 1, 0,
"Apple", 6, 4, 11, 1, 2, 1, 0,
"Berries", 6, 3, 11, 2, 2, 1, 0,
"Steak", 6, 18, 0, 0, 35, 15, 0,
"Apple Pie", 6, 20, 11, 5, 42, 20, 0,
"Health Potion", 6, 30, 0, 0, 50, 23, 0,
"Mana Potion", 11, 20, 0, 0, 40, 17, 0,
"Purple Potion", 6, 30, 11, 20, 80, 40, 0]
#[0]N/A [1]Monster Name [2]LVL Max [3]EXP [4]GLD [5]HP [6]DEF [7]ATT [8]SPD
mstrstts = ["N/A", "Slime", 5, 2, 3, 5, 0, 2, 4,
"Flower Mimic", 7, 20, 13, 12, 2, 3, 2,
"Goblin", 8, 9, 15, 10, 1, 5, 4,
"Skeleton", 10, 20, 23, 15, 1, 5, 1,
"Treasure Mimic", 13, 65, 75, 25, 3, 5, 1,
"Bandit", 20, 80, 50, 20, 3, 6, 3,
"Rock Golem", 10, 125, 25, 30, 5, 8, 1,
"Flame Dragon", 5, 800, 200, 125, 3, 10, 6]
#misc defs
mstrenc = 0
def expdisplay():
    exp1 = round(21 / playerstts[4] * playerstts[3])
    exp2 = "#" * exp1
    exp3 = 21 - exp1
    exp4 = "-" * exp3
    print(f"[{exp2}{exp4}]")
    return ""
def checkplayerstts():
    print(f"{playerstts[1]}'s Stats:")
    print(f"LVL {playerstts[2]}, EXP {playerstts[3]}/{playerstts[4]}")
    print(f"{expdisplay()}")
    print(f"Gold: {playerstts[5]}")
    print(f"HP: {playerstts[6]}/{playerstts[7]}")
    print(f"Defense: {playerstts[8]}")
    print(f"Attack: {playerstts[9]}")
    print(f"Magic Attack: {playerstts[10]}")
    print(f"Mana: {playerstts[11]}/{playerstts[12]}")
    print(f"Speed: {playerstts[13]}")
def levelupcheck():
    levelupadddisplay = 0
    while True:
        if playerstts(3) > playerstts(4):
            playerstts(3) == playerstts(3) - playerstts(4)
            playerstts(2) == playerstts(2) + 1
            levelupadddisplay = levelupadddisplay + 1
    print(f"{playerstts(1)}'s level went up by {levelupadddisplay}! ")
#title/intro
print("Pyknight v2.1")
print("---------------------------------")
#load/save/naming
while True:
    print("Name your character: (16 or less characters) ")
    playerstts[1] = input("")
    print("---------------------------------")
    if len(playerstts[1]) < 17:
        if len(playerstts[1]) > 0:
            if playerstts[1] == "Default":
                print("Invalid character name.")
                print("Please try a new name.")
                print("---------------------------------")
            else:
                break
        else:
            print("The name entered contains no characters.")
            print("Please try a new name.")
            print("---------------------------------")
    else:
        print("The name entered contains more than 16 characters.")
        print("Please try a new name.")
        print("---------------------------------")
print(f"Welcome to Pyknight, {playerstts[1]}!")
storyword = "start"
print("---------------------------------")
checkplayerstts()
print("---------------------------------")
#the game
while True:
    print(f"How would you like to {storyword} your adventure? (q to quit):")
    storyword = "continue"
    print("[1] Check Stats")
    print("[2] Check Inventory")
    print("[3] Travel")
    print("[4] Sleep")
    storyopt1 = input("")
    print("---------------------------------")
    if storyopt1 == "1":
        checkplayerstts()
    elif storyopt1 == "2":
        checkplayerinv()
    elif storyopt1 == "3":
        mstrwheel = random.randint(1,100)
        if mstrwheel > 0 and mstrwheel < 41:
            mstrenc = 1
        elif mstrwheel > 40 and mstrwheel < 71:
            mstrenc = 17
        elif mstrwheel > 70 and mstrwheel < 91:
            mstrenc = 9
        else:
            mstrenc = 25
        print(f"An enemy {mstrstts[mstrenc]} approached!")
        print("---------------------------------")
        while True:
            randommstrlvl = mstrstts[mstrenc + 1] - random.randint(0, mstrstts[mstrenc + 1] - 1)
            print(f"{mstrstts[mstrenc]}, LVL {randommstrlvl}")
            mstr1hpcurrent = mstrstts[mstrenc + 4] + round(randommstrlvl / 10)
            print(f"HP: {mstr1hpcurrent}/{mstrstts[mstrenc + 4] + round(randommstrlvl / 10)}, DEF: {mstrstts[mstrenc + 5]}")
            if int(mstrstts[mstrenc + 7] + round(randommstrlvl / 10)) > playerstts[13] or int(mstrstts[mstrenc + 7] + round(randommstrlvl / 10)) == playerstts[13]:
                print(f"what will {playerstts[1]} do?")
                print(f"[1] Attack | {playerstts[9] - mstrstts[mstrenc + 5]}+")
                print(f"[2] Magic  |")
                print(f"[3] Item   |")
                print(f"[4] Flee   |")
                battleopt = input("")
                if battleopt == "1":
                    playerdam1 = playerstts[9] - mstrstts[mstrenc + 5] + random.randint[0, 2]
                    print(f"You dealt {playerdam1} damage!")
            else:
                print(f"The {mstrstts[mstrenc]} outsped you!")
                mstrdam1 = mstrstts[mstrenc + 6] - playerstts[8]
                print(f"The {mstrstts[mstrenc]} dealt 
                      {mstrdam1} damage!")
        print("---------------------------------")
    elif storyopt1 == "4":
        sleep()
    elif storyopt1 == "q":
        break
    else:
        print("Invalid Input, please try again.")
        print("---------------------------------")
print("Exiting Pyknight...")
