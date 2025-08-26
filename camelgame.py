import random # Point 2
import os

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


while not done:
    if miles_traveled == 0 and thirst == 0 and camel_tiredness == 0 and natives_traveled == -20 and canteen == 3:
        print("""
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
    """)
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.") 
    # ^ Point 1

    choice = input("Your choice: ").upper()

    if choice == "Q":
        print("You quit the game.")
        done = True

    elif choice == "A":
        if canteen > 0:
            canteen -= 1
            thirst = 0
            print("You take a drink. Thirst is gone.")
        else:
            print("You have no drinks left!")

    elif choice == "B":
        miles = random.randint(5, 12)
        miles_traveled += miles
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randint(7, 14)
        print(f"You traveled {miles} miles at moderate speed.")

    elif choice == "C":
        miles = random.randint(10, 20)
        miles_traveled += miles
        thirst += 1
        tired = random.randint(1, 3)
        camel_tiredness += tired
        natives_traveled += random.randint(7, 14)
        print(f"You traveled {miles} miles at full speed. Camel tiredness increased by {tired}.")

    elif choice == "D":
        camel_tiredness = 0
        print("You stop for the night. Your camel is happy.") # fixed spelling
        natives_traveled += random.randint(7, 14)

    elif choice == "E":
        print(f"\nMiles traveled:  {miles_traveled}")
        print(f"Drinks in canteen:  {canteen}")
        print(f"The natives are {miles_traveled - natives_traveled} miles behind you.")

    # Oasis event
    if not done and random.randint(1, 10) == 1:
        print("\nYou found an oasis!")
        canteen = 3
        thirst = 0
        camel_tiredness = 0
        print("Your canteen is refilled, thirst quenched, and camel rested!")

    # check game conditions
    if choice != "E":
        if not done and thirst >= 6:
            print("You died of thirst!")
            done = True
        elif not done and thirst >= 4:
            print("You are thirsty!")

        if not done and camel_tiredness > 8:
            print("Your camel has died!")
            done = True
        elif not done and camel_tiredness >= 5:
            print("Your camel is getting tired.")

        if not done and natives_traveled >= miles_traveled:
            print("The natives have caught up with you! You lose!")
            done = True
        elif not done and (miles_traveled - natives_traveled) < 15:
            print("The natives are getting close!")

        if not done and miles_traveled >= 100:
            print("You made it across the desert! You won!")
            done = True

    # Clear Console Functionality Fix (To-Do)
    if not done:
        input("\nPress Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    
    