from functools import reduce

n = int(input())
C = (25, 10, 5, 1)

def coin_count(amount, coins):
    return reduce(
        lambda acc, c: (acc[0] + (q := acc[1] // c), acc[1] % c),
        coins,
        (0, amount)
    )[0]

print(coin_count(n, C))