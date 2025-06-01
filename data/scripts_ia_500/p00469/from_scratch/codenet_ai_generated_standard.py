from itertools import permutations

while True:
    n = int(input())
    if n == 0:
        break
    k = int(input())
    cards = [input().strip() for _ in range(n)]
    results = set()
    for p in permutations(cards, k):
        results.add(''.join(p))
    print(len(results))