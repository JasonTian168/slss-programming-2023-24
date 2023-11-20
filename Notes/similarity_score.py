hobbies1 = input("Please enter hobbies, separated by spaces ").lower().split()

hobbies2 = input("Please enter another set of hobbies, separated by spaces ").lower().split()

similarScore = 0

for hobbies in hobbies1:
    if hobbies in hobbies2:
        similarScore += 1

print("You have " + str(similarScore) + " hobbies in common!")
