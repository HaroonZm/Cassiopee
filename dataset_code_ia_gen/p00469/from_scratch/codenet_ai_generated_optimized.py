import sys
from itertools import permutations

input = sys.stdin.readline

while True:
    n = int(input())
    k = int(input())
    if n == 0 and k == 0:
        break
    cards = [input().strip() for _ in range(n)]
    results = set()
    for seq in permutations(cards, k):
        results.add(''.join(seq))
    print(len(results))