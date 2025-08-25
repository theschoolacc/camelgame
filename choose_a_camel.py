# class Camel:
#     def __init__(self, camel_type):
#         self.camel_type = camel_type
#         if camel_type == "Dromedary":
#             self.max_tiredness = 8
#             self.speed_range = (10, 20)
#         elif camel_type == "Bactrian":
#             self.max_tiredness = 10
#             self.speed_range = (8, 16)
#         else:
#             self.max_tiredness = 7
#             self.speed_range = (5, 12)
#         self.tiredness = 0

#     def travel(self, fast=False):
#         if fast:
#             miles = random.randint(*self.speed_range)
#             self.tiredness += random.randint(1, 3)
#         else:
#             miles = random.randint(5, 12)
#             self.tiredness += 1
#         return miles

# # At game start:
# print("Choose your camel type:")
# print("1. Dromedary (fast, less endurance)")
# print("2. Bactrian (slower, more endurance)")
# print("3. Wild Camel (average)")
# camel_choice = input("Enter 1, 2, or 3: ")
# camel_types = { "1": "Dromedary", "2": "Bactrian", "3": "Wild Camel" }
# player_camel = Camel(camel_types.get(camel_choice, "Wild Camel"))