name = input("What is your name?")
print(f"Nice to meet you" + " " + name)

location = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctica"]
index = 0
sum = 0
NUMS_RESPONDENTS = 7

for _ in range(NUMS_RESPONDENTS):
    location_question = input("Have you ever been to" + " " + str(location[index])).strip(",.?!").lower() 
    index +=1
    if location_question == "yes":
        sum += 1

print("You have been to" + " " + str(sum) + " /" + " " + str(NUMS_RESPONDENTS) + " countries")
      
    