import sys
from collections import Counter

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))

N = I()
A = LI()
counter = Counter(A)
unique_count = len(counter)
duplicates = sum(count - 1 for count in counter.values())

print(unique_count - (duplicates & 1))