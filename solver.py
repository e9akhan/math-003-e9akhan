from math import sqrt, ceil

def solver(value):

    factors = []
    max_factor = 0

    for i in range(2,ceil(sqrt(value))):
        if value%i==0:
            factors.append(i)
            factors.append(value//i)

    if len(factors)==0:
        return value

    for factor in factors:
        flag = 0
        for i in range(2,ceil(sqrt(factor))):
            if factor%i==0:
                flag = 1
                break
        
        if flag==0:
            max_factor = factor
    return max_factor
