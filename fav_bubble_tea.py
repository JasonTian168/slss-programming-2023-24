# Bubble Tea Popularity Algorithm
# Author: Jason Tian
# Date: 27 October 2023

# Ask 5 user what their favourite bubble tea placen is
# Prints out a summary if the data.

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
bubqueen_likes = 0

NUM_RESPONDENTS = 5

for _ in range(NUM_RESPONDENTS):
# Ask the user what their favourite plce is
    print("What's your favourite bubble tea place?")


    fave_place = input().strip(",.?!").lower()
    # Tally or counting algo
    if fave_place == "coco":
        coco_likes += 1
    elif fave_place == "suntea":
        suntea_likes += 1
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
# Print out a summary of all the placescoco


# Give the raw score and the percentage
total = coco_likes + chatime_likes + suntea_likes + bubqueen_likes
print(f"CoCo likes : {coco_likes}")
print("The Percentage is: " + str(coco_likes / total * 100) + "%")
print(f"Chatime likes : {chatime_likes}")
print("The Percentage is: " + str(chatime_likes / total * 100) + "%")
print(f"Suntea likes : {suntea_likes}")
print( "The Percentage is: " + str(suntea_likes / total * 100) + "%")
print(f"Bubble Queen likes : {bubqueen_likes}")
print( "The Percentage is: " + str(bubqueen_likes / total * 100) + "%")

print("HI")

