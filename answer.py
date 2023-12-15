"""
    Module name :- answer
    Method(s) :- answer()
"""

from solver import solver

def answer():
    """
    Find the largest prime factor of 600851475143.
    """
    return solver(600851475143)


if __name__ == "__main__":
    print(answer())
