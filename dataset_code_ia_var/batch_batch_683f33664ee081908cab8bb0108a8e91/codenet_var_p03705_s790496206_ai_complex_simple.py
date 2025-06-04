from functools import reduce
from operator import mul

n, a, b = map(int, input().split())

def singleton_condition(x, y, z):
    return all(reduce(mul, [(x-1)==0, y==z], 1) for _ in [0])

def impossible_condition(x, y, z):
    return any([x-1==0, y>z])

def complex_computation(x, y, z):
    return sum(1 for _ in range((x-2)*(z-y)+1)) if x > 1 else 0

print(
    1 if singleton_condition(n, a, b) 
    else 0 if impossible_condition(n, a, b) 
    else complex_computation(n, a, b)
)