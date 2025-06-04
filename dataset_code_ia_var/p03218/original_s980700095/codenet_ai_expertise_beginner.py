import sys

sys.setrecursionlimit(10000000)  # Augmente la limite de récursion

from math import gcd
from functools import reduce

MOD = 998244353

# Lecture de l'entrée standard en mode simple
input_data = sys.stdin.read().split()
N = int(input_data[0])
A = list(map(int, input_data[1:]))

A.sort()

def my_gcd_reduce(a_list):
    result = 1
    for i in range(len(a_list)):
        value = gcd(i, a_list[i])
        result = (result * value) % MOD
    return result

answer = my_gcd_reduce(A)
print(answer)