import random

class CamelGame:
    print("Welcome to the Camel Game...")
    gather_speed = int(input("To start, type a speed (MPH)..."))
    
    if gather_speed >= 20:
        print("Too fast for a camel, please choose a speed under 20MPH.")
    
    else:
        print(f"Sound good, confirm {gather_speed}"...)
