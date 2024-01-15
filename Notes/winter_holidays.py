# Winter Holidays
# Author: Tian
# Jan 8 2024

import random 
def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - string that indicates whether the event
            is good or bad

    Returns:
        an event that happened to you during the holidays
        the event is selected part"""
    


    good = ["A", "b", "c", "d"]
    bad = ["e", "f", "g"]

    if good_or_bad.strip().lower() == "good":
        return random.choice(good)

    else:
        return random.choice(bad)


def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday("good"))
    # "I got a Lego set for the first time in a long time."
    # "I went to Richmond Centre to walk around aimlessly."
    print(winter_holiday("bad"))
    # "I hoped to snowboard during the holiday and there was only rain."
    # "I asked for a bidet for Christmas, instead I got a rando smart watch amazon."


# If we're running THIS FILE using Python
if __name__ == "__main__":
        main()
