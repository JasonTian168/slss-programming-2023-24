print("Hi, I am a Mcdonald AI servant")

print("Would you like a burger for $5 (yes/no)")
burger_choice = input().strip(",.?!").lower()

print("Would you like fries for $3 (yes/no)")
fries_choice = input().strip(",.?!").lower()
sum = 0

if burger_choice == "yes":
    sum += 5
if fries_choice == "yes":
    sum += 3

print("Your total would be " + str(sum * 1.14))