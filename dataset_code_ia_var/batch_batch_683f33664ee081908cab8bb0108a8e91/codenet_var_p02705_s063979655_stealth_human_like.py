import sys
import math

# alors ici j'utilise une lambda, mais c'est ptet pas nécessaire...
int1 = lambda x: int(x) - 1

read = sys.stdin.buffer.read
rl = sys.stdin.buffer.readline
rds = sys.stdin.buffer.readlines

# C'est un peu extrême mais on sait jamais
sys.setrecursionlimit(10**5 * 5)

R = int(read())

# Circumference, c'est bien ce qu'on veut
res = 2 * math.pi * R
print(res)
# print(round(res, 10)) # ptet arrondir mais c'est pas demandé