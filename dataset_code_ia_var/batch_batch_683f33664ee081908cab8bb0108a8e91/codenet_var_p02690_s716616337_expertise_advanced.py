from sys import stdin
from itertools import product

x = int(stdin.readline())

powers = {i: i**5 for i in range(-1000, 1000)}
pow_inv = {v: i for i, v in powers.items()}

for a in range(-1000, 1000):
    b5 = a**5 - x
    if b5 in pow_inv:
        print(a, pow_inv[b5])
        break