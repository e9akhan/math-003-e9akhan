"""
    Module name :- solver
    Method(s) :- solver()
"""

from math import sqrt, ceil

def solver(value):
    """
    Find the largest prime factor of a given number.

    Args:
        value(int) :- Number whose largest prime factor to be found.

    Return:
        Return the largest prime factor of a given number.
    """
    factors = []
    max_factor = 0

    for i in range(2, ceil(sqrt(value))):
        if value % i == 0:
            factors.append(i)
            factors.append(value // i)

    if len(factors) == 0:
        return value

    for factor in factors:
        flag = 0
        for i in range(2, ceil(sqrt(factor))):
            if factor % i == 0:
                flag = 1
                break

        if flag == 0:
            max_factor = factor
    return max_factor


if __name__ == "__main__":
    print(f"solver(value=851239123) = {solver(value=851239123)}")
