# Syntax Errors

These types of errors are ones where you run your code and something breaks.

Syntax errors are really easy to fix

Syntax errors happen when we don't follow the rules completely.

Some examples are when we forget a closing. Or if we are missing a closing parenthesis.

# Semantic Errors

Semantic Errors are much more challenging to squash

Semantic errors are where you code doesn't "mean" what you actually mean.

```python
user_response = input("Do you like to eat food? ")

if user_response == "yes":
	print("you passed the human test")

else:
print("You must be some sort of robot.")
```

The problem with the above code is subtle. What I mean is that if the users use anything affirmative the code should go into "yes" block.


One way to solve the problem is to use [[Strings#String Methods]]. We can use .lower to catch all permutations of capital letters.

```python
user_response = input("Do you like to eat food? ")

if user_response.lower() == "yes":
	print("you passed the human test")

else:
print("You must be some sort of robot.")
```