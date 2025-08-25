import random
import os

print("Welcome to the Camel Game!")
print("You’ve taken a camel to journey across the vast Sahara desert.")
print("The locals are pursuing you to reclaim their camel.")
print("Endure your desert adventure and stay ahead of the natives.\n")

# Variables
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20   # start 20 miles behind
canteen = 3
done = False

while not done:
    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

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
        camel_tiredness += random.randint(1, 3)
        natives_traveled += random.randint(7, 14)
        print(f"You traveled {miles} miles at full speed.")

    elif choice == "D":
        camel_tiredness = 0
        print("You stop for the night. Your camel is happy.")
        natives_traveled += random.randint(7, 14)

    elif choice == "E":
        print(f"\nMiles traveled: {miles_traveled}")
        print(f"Drinks in canteen: {canteen}")
        print(f"Thirst: {thirst}")
        print(f"Camel tiredness: {camel_tiredness}")
        print(f"The natives are {miles_traveled - natives_traveled} miles behind you.")

    # random oasis event
    if not done and random.randint(1, 20) == 1:
        print("\nYou found an oasis!")
        canteen = 3
        thirst = 0
        camel_tiredness = 0
        print("Your canteen is refilled, thirst quenched, and camel rested!")

    # check game conditions
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
        print("The natives are close!")

    if not done and miles_traveled >= 200:
        print("Congratulations! You crossed the desert and won!")
        done = True

    # Clear console each loop (optional for Windows)
    # os.system("cls")
