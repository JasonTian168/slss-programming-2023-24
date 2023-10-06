# Foods Suggestion Bot
# Author: Tiam
# 6 October 2023

# A bot that asks the user what ther favourtie food
# fodd is. Based on that food, it wil classify
# the type/genre/cuisine of the food, then
# give a resturant a suggestion

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am a bot here to recommend a resturant")
time.sleep(1)
fav_food = input("To help me suggest a resturant, can you tell me what your favourite food?")
time.sleep(1)

# Italian Cuisisne
italian_food = ["pasta", "pizza", "cannelont", "tiramisu"]
# If they answer Italian with Italian food, suggest an Italian resturant.
if fav_food.lower().strip("!.,?") in italian_food:
    print("I see that you may like Italian food.")
    time.sleep(1)
    print("I suggestThe Old Spaghetti Factory. The address is: 14200 Entertainment Blvd #110, Richmond, BC V6W 1K3 ")
else:
    print("Sorry I unfortunatly don't know what type of food you replied is")