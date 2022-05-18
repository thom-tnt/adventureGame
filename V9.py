
# Game title: Text Adventure Game (10D
# Version 9.0
# Created: Friday 25th March 2022
# Last Modified: Monday 9th may 2022
import time
import random
from random import choice


global monsterLoot
monsterLoot = ["hide","Teeth"]
global RareMonsterDrop
RareMonsterDrop = ["Sharp horn","a","a","a","a"]
global monsterKnife
monsterKnife = ["a dull bone knife"]
global backpack
backpack = []
global bag
bag = ["10 10p coins", "an arrow" , "a Steak" , "Bones"]
global chest
chest = ["10 10p coins", "a bow","an arrow","a kinfe"," an axe","a Steak","Cooked chicken","a Mimic!","a Staff"]
global health
health = 100
global strength
strength = 0
global vitality
vitality = 0


#--------------FIRST CHOICE

def FirstChoice(health):                                         #First choice
        print("would you like to go left or right?")
        Choice1 = input(":")
        Choice1 = Choice1.lower()

        if Choice1 == "left":
            print ("The road it is!")
            ch1Left(health)
            
        elif Choice1 == "right":
            print("The dirt path it is. Try not to fall it's a rough path!")
            ch1Right(health)
            
        else:
            print("Invalid Choice! Please Type left or right.")
            FirstChoice(health)

    #-------------CHOICE 1 RIGHT

def ch1Right(health):
    print("you get about half way down the path and fall over see a chest")
    print("do you want to open the chest?")
    ChestChoice1 = input (": ")
    ChestChoice1 = ChestChoice1.lower()
    
    if ChestChoice1 == "yes":
        ChestLoot1 = random.choice(chest)
        print ("you found", ChestLoot1)
        backpack.append(ChestLoot1)
        print(ChestLoot1 , "was added to your backpack.")
        separator = ","
        print("you now have" , separator.join(backpack) , "In your bag")
        print("you carry on down the path")
    elif ChestChoice1 == "no":
        print("you carry on down the path")
    else:
        print("Invalid Choice! Please Type yes or no.")
        ch1Right(health)


# ------CHOICE 1 LEFT

def ch1Left(health):
    print("you go down the road and see a group of monsters through the trees.")
    print("the monsters are about to leave their camp do you want to steal their items after they leave?")

    RaidMonChoice = input (": ")
    RaidMonChoice = RaidMonChoice.lower()
    
    if RaidMonChoice == "yes":
        print ("You enter the monster camp without a sound and you think the monsters have all left.")
        print ("there is a bag you can loot but also a tent Which would you like to Loot?")
        print ("Bag or Tent?")
        BagTent(health)
    elif RaidMonChoice == "no":
        print ("You carry on down the path")
    else:
        print ("Invalid Choice! Please Type yes or no.")
        ch1Left(health)

#------BAG TENT CHOICE

def BagTent(health):
    bagTentChoice = input (": ")
    bagTentChoice = bagTentChoice.lower()

    if bagTentChoice == "bag":
        bagLoot = random.choice(bag)
        print ("You have looted the bag and got", bagLoot)
        print (bagLoot , "has been addded to your backpack")
        backpack.append(bagLoot)
        separator = ","
        print ("you now have" , separator.join(backpack) , "In your bag")
    elif bagTentChoice == "tent":
        print ("There is a sleeping monster in the tent!")
        print ("You can leave or try to take the Knife next to him but you may wake him up!")
        print ("Do you want to take the knife?")
        MonKnife(health)
    else:
        print ("Invalid Choice! Please Type bag or tent")
        BagTent(health)

#---------MONSTER KNIFE CHOICE

def MonKnife(health):
    MonKnifeChoice = input (": ")
    MonKnifeChoice = MonKnifeChoice.lower()

    if MonKnifeChoice == "yes":
        print("You try and take the knife but wake the monster")
        print("The monster wakes up and sees you!")
        print("what do you do? Run or Fight!")
        MonFight(health)
    elif MonKnifeChoice == "no":
        print ("You turn from the tent.")
        print ("You can still loot the bag before you leave.")
        print ("Do you want to loot the bag or not?")
##        Greed1(health)
    else:
        print ("Invalid Choice! Please Type yes or no.")
        MonKnife(health)

#------------MONSTER FIGHT 1

def MonFight(health):
    MonFightChoice = input (": ")
    MonFightChoice = MonFightChoice.lower()

    if MonFightChoice == "fight":
        print("Do you want to go for the knife or punch him while he is still off guard")
        MonFight2(health)
    elif MonFightChoice == "run":
        print("You got away before he could be on full aleart and you carry on back down the road")
    else:
        print("Invalid Choice! Please type run or fight.")
        MonFight(health)
        
#---------MONSTER FIGHT 2

def MonFight2(health):
    MonFight2Choice = input (": ")
    MonFight2Choice = MonFight2Choice.lower()

    if MonFight2Choice == "knife":
        print("You lunge for the knife and stand guard")
        backpack.extend(monsterKnife)
        for items in backpack:
                correctedItems = (", " .join (items))
        print ("You now have",correctedItems,"in your backpack!!!")
        print("The monsters attacks are slow and you are able to evade his first punch.")
        print("Do you want to stab left or right")
        MonFight3(health, strength)
    elif MonFight2Choice == "punch":
        print("You punch him but it is in effective.")
        print("The monster was able to grab you.")
        print("You died.")
        health = health - 101
    else:
        print("Invalid Choice! Please type punch or knife.")
        MonFight2(health)
        
#--------MONSTER FIGHT 3

def MonFight3(health, strength):
    MonFight3Choice = input (": ")
    MonFight3Choice = MonFight3Choice.lower()

    if MonFight3Choice == "left":
        print("The monster predicted your move!")
        print("You were slashed on your right arm and are now bleeding")
        print("The blow wasn't deep but the bleading could be fatal")
        print("The monsters blow did 25 damage!")
        print("You are now bleading for 5 damage each turn.")
        damage = int(5)
        health = health - damage
        health = health - 25
        print ("Your health is now at" , health , "HP")
    elif MonFight3Choice == "right":
        Mon1Health = 150
        print ("You dealt a fatal blow to the monster!!!")
        print ("The monster is stunned from the blow")
        Mon1Health = Mon1Health - 75
        print("The monster is now at" , Mon1Health , "Health")
        print ("Your Strength raised by one")
        strength = strength + 1
        print("your strength has raised to" , strength)
        print("The monster still stunned is unable to move do you wish to attack again or attempt to escape?")
        MonFight4(health, strength, Mon1Health)
    else:
        print ("invalid choice! Please type left or right")
        MonFight3(health, strength)

#--------------Monster Fight 4

def MonFight4(health, strength, Mon1Health):
    MonFight4Choice = input (": ")
    MonFight4Choice = MonFight4Choice.lower()

    if MonFight4Choice ==  "attack":
            print("You attack again!")
            Mon1Health = Mon1Health - 75 + strength
            if Mon1Health > 0:
                MonLoot1 = []
                MonLoot1 = MonLoot1 + monsterLoot
                RareItem = random.choice(RareMonsterDrop)
                if RareItem == "Sharp horn":
                        MonLoot1 = MonLoot1 + RareItem
                Separator = ','
                print ("You recieved", Separator.join(MonLoot1))
                backpack.extend(MonLoot1)
                print(backpack)
                for items in backpack:
                        correctedItems = (", " .join (items))
                print("The monster died. You now have", correctedItems , "in your inventory")
                
        
        

#MAIN
print ("Steve: Hello there I've never seen you around these parts you must be a Traveller!")
#time.sleep(3)
print ("Steve: Before you enter Lavender Town I do warn you that it is rumoured that most pedestrians who enter this town do not come out of this alive!")
#time.sleep(4)
print ("Steve: People who have have said it causes many illusions and have barely escaped with their lives. This is because of the monsters and evil beings which lurk within!")
#time.sleep(5)
print ("Steve: Well! let me introduce myself I'm Steven Stone nice to meet you!")
#time.sleep(3)


user = input("And you might be? : ")                 #Inputing the player username
print ("Well thats an interesting name you have there" , user ,"!")

print("Steve: Well" , user , "you can either follow the road to the left or go right down the dirt path")
#time.sleep(3)
print("Steve: It is said more people survive going down the dirt path but you do not have to trust me I'm but a lowley a stranger.")
#time.sleep(4)

FirstChoice(health)
while health > 0:
    print("GAME OVER!!!")
    exit()
