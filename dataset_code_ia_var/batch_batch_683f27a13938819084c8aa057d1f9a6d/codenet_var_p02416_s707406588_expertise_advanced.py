from sys import stdin
from functools import reduce

def sum_of_digits(number: str) -> int:
    return reduce(lambda acc, digit: acc + int(digit), number, 0)

for line in map(str.strip, stdin):
    if line == '0':
        break
    print(sum_of_digits(line))