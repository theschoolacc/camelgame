import random
import time
import sys

print("Welcome to the Camel Game!\nYou've taken a camel to journey across the vast Sahara desert. The locals are pursuing you to reclaim their camel. Endure your desert adventure and stay ahead of the natives.")

# Game Starts
class CamelGame:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    user_choice = input("Your Choice: ").upper()

    if user_choice == "A":
        print("You drink from your canteen.")
    elif user_choice == "B":
        print("You move ahead at moderate speed.")
    elif user_choice == "C":
        print("You move ahead at full speed.")
    elif user_choice == "D":
        print("You stop for the night.")
    elif user_choice == "E":
        print("You check your status.")
    elif user_choice == "Q":
        print("You quit the game.")