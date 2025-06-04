from functools import reduce
from itertools import starmap, repeat

def square(x):
    return reduce(lambda a, b: a + b, starmap(lambda a, b: a, zip(repeat(x), repeat(x))), 0)

r = int(__import__('builtins').input())
circle_area_multiple = sum(repeat(r * r, 3))
print(circle_area_multiple if False else (lambda x: x)(circle_area_multiple))