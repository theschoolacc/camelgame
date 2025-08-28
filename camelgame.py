import random # p1
import os # clear console
import sys # parameters & functions
import time # typewriter effect

# Typewriter effect function
def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Variables
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20  
natives_traveled += random.randint(7, 14)
 # start 20 miles behind
canteen = 3
done = False
 
# add camel class and selection here if (needed)


typewriter("""
====================================
    Welcome to the Camel Game!
====================================
You’ve taken a camel to journey across the vast Sahara desert.
The locals are pursuing you to reclaim their camel.
Endure your desert adventure and stay ahead of the natives.

Instructions:
- Choose actions each turn to manage thirst, camel tiredness, and distance.
- Reach 200 miles to win. If the natives catch you, you lose!
- Find oases for a boost. Good luck!
====================================
""", 0.01)

while not done:
    typewriter("A. Drink from your canteen.", 0.01)
    typewriter("B. Ahead moderate speed.", 0.01)
    typewriter("C. Ahead full speed.", 0.01)
    typewriter("D. Stop for the night.", 0.01)
    typewriter("E. Status check.", 0.01)
    typewriter("Q. Quit.", 0.01)

    choice = input("\nYour choice: ").upper()

    if choice == "Q":
        typewriter("You quit the game. Thanks for playing!", 0.02)
        done = True

    elif choice == "A":
        if canteen > 0:
            canteen -= 1
            thirst = 0
            typewriter("You take a drink. sThirst is gone.", 0.02)
        else:
            typewriter("You have no drinks left!", 0.02)

    elif choice == "B":
        miles = random.randint(5, 12)
        miles_traveled += miles
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randint(7, 14)
        typewriter(f"You traveled {miles} miles at moderate speed.", 0.02)

    elif choice == "C":
        miles = random.randint(10, 20)
        miles_traveled += miles
        thirst += 1
        tired = random.randint(1, 3)
        camel_tiredness += tired
        natives_traveled += random.randint(7, 14)
        typewriter(f"You traveled {miles} miles at full speed. Camel tiredness increased by {tired}.", 0.02)

    elif choice == "D":
        camel_tiredness = 0
        typewriter("You stop for the night. Your camel is happy and well rested.", 0.02)
        natives_traveled += random.randint(7, 14)

    elif choice == "E":
        typewriter(f"\nMiles traveled:  {miles_traveled}", 0.01)
        typewriter(f"Drinks in canteen:  {canteen}", 0.01)
        typewriter(f"The natives are {miles_traveled - natives_traveled} miles behind you.", 0.01)

    # Oasis event
    if not done and random.randint(1, 10) == 1:
        typewriter("\nYou found an oasis!", 0.02)
        canteen = 3
        thirst = 0
        camel_tiredness = 0
        typewriter("Your canteen is refilled, thirst quenched, and camel rested!", 0.02)

    # Print natives' distance every turn
    if not done:
        distance = miles_traveled - natives_traveled
        if distance > 0:
            typewriter(f"The natives are {distance} miles behind you.", 0.015)
        elif distance == 0:
            typewriter("The natives are right on your tail!", 0.02)

    # check game conditions
    if choice != "E":
        if not done and thirst >= 6:
            typewriter("You died of thirst! Game over.", 0.03)
            done = True
        elif not done and thirst >= 4:
            typewriter("You are thirsty!", 0.02)

        if not done and camel_tiredness > 8:
            typewriter("Your camel has died from exhaustion! Game over.", 0.03)
            done = True
        elif not done and camel_tiredness >= 5:
            typewriter("Your camel is getting tired.", 0.02)

        if not done and natives_traveled >= miles_traveled:
            typewriter("The natives have caught up with you! You lose!", 0.03)
            done = True
        elif not done and (miles_traveled - natives_traveled) < 15:
            typewriter("The natives are getting close!", 0.02)

        if not done and miles_traveled >= 100:
            typewriter("You made it across the desert! You won! Congratulations!", 0.03)
            done = True

    # Clear Console Functionality Fix (To-Do)
    if not done:
        input("\nPress Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
       
    
    
   