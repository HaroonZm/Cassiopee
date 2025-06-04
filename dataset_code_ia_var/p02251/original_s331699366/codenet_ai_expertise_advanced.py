from functools import reduce
import sys

def min_coins(amount, denominations=(25, 10, 5, 1)):
    return reduce(
        lambda acc, d: (acc[0] + acc[1] // d, acc[1] % d),
        denominations,
        (0, amount)
    )[0]

print(min_coins(int(sys.stdin.readline())))