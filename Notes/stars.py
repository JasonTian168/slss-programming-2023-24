def stars(nums_stars: int) -> str:
    return "*" * nums_stars

print(stars(10))

def biggest_of_three(num_one: int, num_two: int, num_three: int) -> int:
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_one and num_two > num_three:
        return num_two
    else:
        return num_three

print(biggest_of_three(2, 3, 4))


def pyramid(NUMS_RESPOND: int) -> int:
    for i in range(1, NUMS_RESPOND+1):
        print("*" * i)
    

print(pyramid(5))

