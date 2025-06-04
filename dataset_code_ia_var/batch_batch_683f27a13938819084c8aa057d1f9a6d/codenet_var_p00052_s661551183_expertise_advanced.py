from math import factorial
from itertools import takewhile, count

def count_trailing_zeros(n):
    return sum(1 for _ in takewhile(lambda x: x == '0', str(factorial(n))[::-1]))

if __name__ == '__main__':
    for n in iter(lambda: int(input()), 0):
        print(count_trailing_zeros(n))