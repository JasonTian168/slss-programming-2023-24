In Python, data can be grouped in categories in types.

| Name     | Example       |
| ---      | ---           |
| string   |  "hello"      |
| list     | [1, 2, 3, 4]  |
| int      | 1, 2, 3, 4    |
| float    | 3.5, -3.5, 1.0|
| boolean  | True or False |




An example pf using these types of data:

```python
favourite_food = "tempura"
my_age = 16
```

## Type Conversion

In python, there are some special functions that allows us to change he type of something 

```python
intro string = "My age is"      # type string
may_age = 50                    # type int

# Aside
"My name is" + "Slim Shady"     # "My name isSlimShady"

print(intro_string + my_age).  # This breaks
```
We can use the following built in function to convert into different types:

```python
int()
float()
str()
list()
```

We can fix the example above in this w ay:

```python
intro_string = "My age is"
my_age = 16

print(intro_string + str(my_age))
print(intro_string + " " + str(my_age))   
print(f"{intro_string} + " " + {my_age}")  
```