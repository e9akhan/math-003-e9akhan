from math import sqrt, ceil
import time

def solver(value):
    start = time.perf_counter()

    factors = []
    max_factor = 0

    for i in range(2,ceil(sqrt(value))):
        if value%i==0:
            factors.append(i)
            factors.append(value//i)

    for factor in factors:
        flag = 0
        for i in range(2,ceil(sqrt(factor))):
            if factor%i==0:
                flag = 1
                break
        
        if flag==0:
            max_factor = factor

    end = time.perf_counter()

    print("This func takes:", (end-start))
    return max_factor
