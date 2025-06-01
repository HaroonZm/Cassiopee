from math import ceil

n = int(input())
shop = input()
s = [input() for _ in range(n)]
m = len(shop)

def contains_shop(st):
    length = len(st)
    max_step = 2 * ceil(length / m)
    return any(shop in st[j::k] for j in range(length) for k in range(1, max_step))

print(sum(contains_shop(st) for st in s))