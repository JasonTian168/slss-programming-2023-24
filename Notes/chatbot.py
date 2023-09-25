# Chatbot
# Author: Tian
# Date: 20 September 2023

import random
import time

# Greet the user
print("Hello there!😁 ")
time.sleep(1.5)
print("Im a crude chatbot here to talk to you. ")
time.sleep(1.5)


# Get the user's name and store it in a variable
user_name = input("So... What's your name?")

# Respond with the user's name in a friendly way
print(f"It's good to meet you, {user_name}")

# Get the user's favourite food and store it in a variable
fav_food = input("What is your favourite food?")

# Make a comment about their food and try not to be TOO REPETITIVE
# Create a list of possible responses
list_of_food_responses = [
    f"Oh. I've never had {fav_food} before",
    "Mmmmmm. That sounds good!",
    "I heard that that is delicious.",
    "Cool."
]


# Choos one of those responses randomly

random_food_response = random.choice(list_of_food_responses)

# Print out that chosen response
print(random_food_response)
