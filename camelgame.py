import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.02):
    """Print text slowly with color for dramatic effect."""
    for char in text:
        print(color + char + Style.RESET_ALL, end="", flush=True)
        time.sleep(delay)
    print()


# --------------------------
# NEW GAME SETUP
# --------------------------
def new_game():
    return {
        "day": 0,
        "miles": 0,
        "goal": 250,        # target distance
        "crew": 18,
        "food": 100,
        "water": 80,
        "armor": 15,
        "morale": 10,
        "gold": 0,
        "shipclass": None,  # Will be set after selection
        "speed": 18,        # Default (Galleon)
    }  
sickness = False
# --------------------------
# MAIN MENU
# --------------------------
# Credits to display  menu
credits = [
    "Game Design: Aria Khanpour",     
    "Coding: Tyler Sims & Aria Khanpour",
    "Prompting: Tyler Sims",
    "Special Thanks: Python Community"
]

def main_menu():
    while True:
        # unique animated credits with fade-in effect
        # Animated "CREDITS" reveal
        for i in range(3):
            print(Fore.MAGENTA + "C R E D I T S".center(40), end="\r", flush=True)
            time.sleep(0.3)
            print(" " * 40, end="\r", flush=True)
            time.sleep(0.2)
        print(Fore.MAGENTA + "C R E D I T S".center(40))
        time.sleep(0.5)
        for line in credits:
            display = [' ' for _ in line]
            for i, char in enumerate(line):
                display[i] = char
            print(Fore.MAGENTA + ''.join(display) + Style.RESET_ALL, end="\r", flush=True)
            time.sleep(0.01)
            print(Fore.MAGENTA + ''.join(display) + Style.RESET_ALL)
            time.sleep(0.05)
        print()
        print(Fore.CYAN + """
  ============================
            VOYAGE OF THE STORMS
        ============================
        1. Start Voyage
        2. Instructions
        3. Quit
        """)
        choice = input(Fore.YELLOW + "> ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            instructions()
        elif choice == "3":
            slow_print("Goodbye, Captain!", Fore.GREEN)
            break
        else:
            slow_print("Invalid choice!", Fore.RED)

# --------------------------
# SHIP CLASS SELECTION
# --------------------------
def ship_class_selection(stats):
    print(Fore.CYAN + """
    Choose your ship class:
    1. Ambassador (Fast, low armor)
    2. Galleon (Balanced)
    3. Voyager (Slow, high armor)
    4. Battleship (Big, and very powerful.)
    """)
    while True:
        choice = input(Fore.YELLOW + "> ").strip()
        if choice == "1":
            slow_print("You chose the Ambassador: swift but fragile.", Fore.GREEN)
            stats["shipclass"] = "Ambassador"
            stats["speed"] = 22
            stats["armor"] = 10
            stats["crew"] = 15
            break
        elif choice == "2":
            slow_print("You chose the Galleon: balanced and reliable.", Fore.GREEN)
            stats["shipclass"] = "Galleon"
            stats["speed"] = 18
            stats["armor"] = 15
            stats["crew"] = 18
            break
        elif choice == "3":
            slow_print("You chose Voyager: slow but tough.", Fore.GREEN)
            stats["shipclass"] = "Voyager"
            stats["speed"] = 14
            stats["armor"] = 22
            stats["crew"] = 20
            break
        elif choice == "4":
            slow_print("You chose Battleship: strong but slow.", Fore.GREEN)
            stats["shipclass"] = "Battleship"
            stats["speed"] = 15
            stats["armor"] = 20
            stats["crew"] = 30
            break
        else:
            slow_print("Invalid choice! Please select 1, 2, 3, or 4.", Fore.RED)
    return stats

# Apply shipclass effects during events
def apply_shipclass_effects(stats, event_type=None):
    # event_type can be 'pirate', 'travel', etc.
    if stats["shipclass"] == "Ambassador":
        if event_type == "pirate":
            # Ambassadors can sometimes avoid pirate fights
            if random.random() < 0.3:
                slow_print("Your swift Ambassador evades the pirates!", Fore.GREEN)
                return "evaded"
        elif event_type == "travel":
            # Faster travel
            return "fast"
    elif stats["shipclass"] == "Voyager":
        if event_type == "pirate":
            # Voyagers take less damage from pirates
            return "tough"
    elif stats["shipclass"] == "Battleship":
        if event_type == "pirate":
            # Battleships deal more damage to pirates
            return "strong"
    # Galleon is balanced, no special effect
    return None

# --------------------------
# INSTRUCTIONS
# --------------------------
def instructions():
    slow_print("""
    Welcome, Captain!
    You must lead your ship and crew across 250 miles of treacherous seas.
    
    Each day you may:
      - Sail forward
      - Rest the crew
      - Fish for food
      - Check status
    
    Beware: storms, pirates, and mutiny may end your journey.
    Mini-games:
      - Pirate Combat: fight turn by turn!
      - Trader Shop: spend gold for supplies.
      - Fishing Challenge: catch more food with luck.
    
    Goal: Survive and reach 250 miles.
    """, Fore.CYAN, 0.01)

# --------------------------
# MINI-GAME: PIRATE COMBAT
# --------------------------
def pirate_combat(stats):
    slow_print("🏴‍☠️ PIRATES attack! Prepare for battle!", Fore.RED)
    # Shipclass effects
    effect = apply_shipclass_effects(stats, event_type="pirate")
    if effect == "evaded":
        return stats
    pirate_health = random.randint(10, 18)
    player_health = stats["armor"] // 2  # ship's battle strength

    while pirate_health > 0 and player_health > 0:
        # Player turn
        if effect == "strong":
            attack = random.randint(4, 9)
        else:
            attack = random.randint(2, 6)
        pirate_health -= attack
        slow_print(f"You hit the pirates for {attack} damage!", Fore.CYAN)
        time.sleep(0.3)

        if pirate_health <= 0:
            break

        # Pirate turn
        if effect == "tough":
            damage = random.randint(1, 3)
        else:
            damage = random.randint(2, 5)
        player_health -= damage
        slow_print(f"The pirates strike back for {damage} damage!", Fore.RED)
        time.sleep(0.3)

    if pirate_health <= 0:
        slow_print("You defeated the pirates!", Fore.GREEN)
        stats["gold"] += random.randint(10, 25)
        stats["morale"] += 1
    else:
        slow_print("You lost the fight! They plunder your ship!", Fore.RED)
        stats["armor"] -= 5
        stats["food"] -= 10
        stats["morale"] -= 2

    return stats

# --------------------------
# MINI-GAME: TRADER SHOP
# --------------------------
def trader_shop(stats):
    slow_print("🛶 A trader ship appears, offering supplies.", Fore.CYAN)
    print(Fore.YELLOW + f"You have {stats['gold']} gold.")
    print("""
    1. Buy Food (10 gold = +20 food)
    2. Buy Water (10 gold = +20 water)
    3. Repair Ship (15 gold = +5 armor)
    4. Leave
    """)
    choice = input("> ")
    if choice == "1" and stats["gold"] >= 10:
        stats["gold"] -= 10
        stats["food"] += 20
        slow_print("You bought food.", Fore.GREEN)
    elif choice == "2" and stats["gold"] >= 10:
        stats["gold"] -= 10
        stats["water"] += 20
        slow_print("You bought water.", Fore.GREEN)
    elif choice == "3" and stats["gold"] >= 15:
        stats["gold"] -= 15
        stats["armor"] += 5
        slow_print("Ship repaired slightly.", Fore.GREEN)
    else:
        slow_print("You sail on without trading.", Fore.CYAN)
    return stats

# --------------------------
# MINI-GAME: FISHING CHALLENGE
# --------------------------
def fishing_challenge(stats):
    slow_print("🎣 The crew sets out to fish...", Fore.CYAN)
    # Guess a number game
    secret = random.randint(1, 5)
    guess = int(input("Guess a number between 1 and 5: "))
    if guess == secret:
        catch = random.randint(15, 25)
        slow_print(f"Jackpot! The crew hauls in {catch} fish!", Fore.GREEN)
    else:
        catch = random.randint(5, 12)
        slow_print(f"You caught {catch} fish.", Fore.GREEN)
    stats["food"] += catch
    stats["water"] -= 2
    return stats

# --------------------------
# RANDOM EVENTS
# --------------------------
def random_event(stats):
    event = random.randint(1, 6)
    if event == 1:
        slow_print("⚡ A STORM smashes the ship!", Fore.BLUE)
        stats["armor"] -= 4
    elif event == 2:
        stats = pirate_combat(stats)
    elif event == 3:
        slow_print("🌴 A hidden island restores your supplies!", Fore.GREEN)
        stats["food"] += 20
        stats["water"] += 15
    elif event == 4:
        slow_print("💀 Sickness spreads among the crew!", Fore.MAGENTA)
        stats["crew"] -= 2
        stats["morale"] -= 1
        killperson = input("throw the sick overboard?(y/n)")
        if killperson == "y":
            crew = crew-1
            sickness =False 
        else:
            sickness=True
            
    elif event == 5:
        slow_print("💰 You find floating treasure!", Fore.YELLOW)
        stats["gold"] += random.randint(10, 30)
    else:
        stats = trader_shop(stats)
    return stats

# --------------------------
# GAME LOOP
# --------------------------
def play_game():
    stats = new_game()
    done = False
    stats = ship_class_selection(stats)

    while not done:
        stats["day"] += 1
        if sickness == True:
            print("some of your crew dies from sickness.")
            crew= crew- random.randint
        print(Fore.CYAN + f"\n--- Day {stats['day']} ---")
        print(Fore.YELLOW + f"Miles: {stats['miles']}/{stats['goal']} | Crew: {stats['crew']} | Food: {stats['food']} | Water: {stats['water']}")
        print(Fore.YELLOW + f"Armor: {stats['armor']} | Morale: {stats['morale']} | Gold: {stats['gold']} | Ship: {stats['shipclass']}")

        print(Fore.CYAN + """
        Choose an action:
        1. Sail forward
        2. Rest crew
        3. Fish for food
        4. Status report
        5. Quit
        """)
        choice = input(Fore.YELLOW + "> ").strip()

        if choice == "1":  # Sail
            effect = apply_shipclass_effects(stats, event_type="travel")
            if effect == "fast":
                travel = random.randint(stats["speed"], stats["speed"] + 8)
            else:
                travel = random.randint(stats["speed"] - 3, stats["speed"] + 4)
            stats["miles"] += travel
            stats["food"] -= 5
            stats["water"] -= 5
            stats["morale"] -= 1
            slow_print(f"You sailed {travel} miles!", Fore.CYAN)
            if random.randint(1, 3) == 1:  # chance of event
                stats = random_event(stats)

        elif choice == "2":  # Rest
            slow_print("The crew rests. Morale rises.", Fore.GREEN)
            stats["morale"] += 2
            stats["food"] -= 3
            stats["water"] -= 3

        elif choice == "3":  # Fishing mini-game
            stats = fishing_challenge(stats)

        elif choice == "4":  # Status
            slow_print("You check the captain’s log... All is recorded.", Fore.CYAN)

        elif choice == "5":  # Quit
            slow_print("You abandon the voyage. Game Over.", Fore.RED)
            break
        else:
            slow_print("Invalid choice!", Fore.RED)

        # --- Check for defeat ---
        if stats["food"] <= 0:
            slow_print("The crew STARVED. Game Over.", Fore.RED)
            done = True
        elif stats["water"] <= 0:
            slow_print("The crew DIES. Game Over.", Fore.RED)
            done = True
        elif stats["morale"] <= 0:
            slow_print("The crew KILLS you. Game Over.", Fore.RED)
            done = True
        elif stats["armor"] <= 0:
            slow_print("The ship SINKS. Game Over.", Fore.RED)
            done = True
        elif stats["crew"] <= 0:
            slow_print("The crew DIES. Game Over.", Fore.RED)
            done = True
        elif stats["miles"] >= stats["goal"]:
            if stats["gold"] > 100:
                slow_print("🏆 You arrive with legendary treasure! You are remembered forever!", Fore.YELLOW)
            elif stats["crew"] <= 5:
                slow_print("💀 You reach land... but with few survivors. A hollow victory.", Fore.MAGENTA)
            else:
                slow_print("🎉 You reached your destination safely. YOU WIN!", Fore.GREEN)
            slow_print(f"Final Score: {stats['gold']} gold collected.", Fore.YELLOW)
            done = True

    again = input(Fore.CYAN + "\nPlay again? (y/n): ").lower()
    if again == "y":
        play_game()
    else:
        slow_print("Farewell, Captain!", Fore.GREEN)
        quit()

# --------------------------
# RUN GAME
# --------------------------
main_menu()