
judge_number = 1
NUMS_RESPONDENTS = 5
sum = 0.0

for _ in range(NUMS_RESPONDENTS):
    judge = float(input("Judge" + str(judge_number) + ": "))
    sum += judge_number
    judge_number += 1

avg_score = sum / NUMS_RESPONDENTS
    

print("Your Olympic Score is: ", avg_score)
