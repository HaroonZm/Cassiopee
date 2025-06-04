from itertools import permutations

while True:
    n = int(input())
    k = int(input())
    if n == 0 and k == 0:
        break
    cards = [input().strip() for _ in range(n)]
    results = set()
    for comb in permutations(cards, k):
        num_str = ''.join(comb)
        results.add(num_str)
    print(len(results))