from functools import reduce
from operator import add

def get_mins(*sizes):
    return (min(map(int, (input() for _ in range(size)))) for size in sizes)

print(reduce(add, get_mins(3, 2)) - 50)