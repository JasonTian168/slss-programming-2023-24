# Functions and Recursion
# Author: Tian
# 6 December 2023

from functools import lru_cache

import time


def factorial(num: int) -> int:
    """Returns the result of the number's
    factorial using recursion

    Params:
        num - number we're calculating

    Returns:
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num - 1) * num


@lru_cache(100)  # with cache/memoization
def fib(n: int) -> int:
    """Calculate and return the nth
    Fibonacci number."""

    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


def fib_itr(n: int) -> int: