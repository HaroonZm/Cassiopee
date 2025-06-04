from itertools import pairwise
from operator import sub
from sys import stdin

N, A, B = map(int, stdin.readline().split())
positions = list(map(int, stdin.readline().split()))
print(sum(min((b - a) * A, B) for a, b in pairwise(positions)))