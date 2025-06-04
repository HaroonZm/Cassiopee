from sys import stdin
from operator import mul

print(mul(*map(int, stdin.readline().split())))