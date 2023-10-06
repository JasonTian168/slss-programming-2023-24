# Format Strings
If we want to evaluate inside of a string, we use f-strings.
To create a f-string, we put an ***f*** before the open quote

```python
fave_food = input("Whats your favorite food")

print(f"Oooooo, {fave_food} sounds good")
```

# String Methods
[[Methods]] are functions that we can use on [[objects]]. 

String methods allow us to modify strings.

Say for example we want to make all the characters of a string lower case.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())
```
We can use String methods to help solve [[Errors#Semantic Errors]]
## .lower()
The .lower() method takes a string and converts all uppercase to lowercase.

## .upper()

The .upper() method takes a string and converts all lowercase to uppercase.

## .strip(chars)
The .strip() method removes characters from both the beginning and the end of the string.

```python
user_feeling = input("How are you feeling today?")

# "good!" "good." "Good!"
if user_feelings.lower().strip("!.,") == good
print("Thats great!")
```

## .split(str)
The `.split()` method splits a string into a [[list]] separating the string based on the characters you give it

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.splt(" ")
```