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
        "gold": 0
    }

# --------------------------
# MAIN MENU
# --------------------------
def main_menu():
    while True:
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
    pirate_health = random.randint(10, 18)
    player_health = stats["armor"] // 2  # ship's battle strength

    while pirate_health > 0 and player_health > 0:
        # Player turn
        attack = random.randint(2, 6)
        pirate_health -= attack
        slow_print(f"You hit the pirates for {attack} damage!", Fore.CYAN)
        time.sleep(0.3)

        if pirate_health <= 0:
            break

        # Pirate turn
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

    while not done:
        stats["day"] += 1
        print(Fore.CYAN + f"\n--- Day {stats['day']} ---")
        print(Fore.YELLOW + f"Miles: {stats['miles']}/{stats['goal']} | Crew: {stats['crew']} | Food: {stats['food']} | Water: {stats['water']}")
        print(Fore.YELLOW + f"Armor: {stats['armor']} | Morale: {stats['morale']} | Gold: {stats['gold']}")

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
            travel = random.randint(12, 25)
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
            slow_print("The crew has NO WATER. Game Over.", Fore.RED)
            done = True
        elif stats["morale"] <= 0:
            slow_print("The crew MUTINIES. Game Over.", Fore.RED)
            done = True
        elif stats["armor"] <= 0:
            slow_print("The ship SINKS. Game Over.", Fore.RED)
            done = True
        elif stats["crew"] <= 0:
            slow_print("All crew are lost. Game Over.", Fore.RED)
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

# --------------------------
# RUN GAME
# --------------------------
main_menu()