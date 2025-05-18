from itertools import permutations as P

while True:
    n, k = int(input()), int(input())
    if k == 0:
        break
    card = [int(input()) for _ in range(n)]
    print(len(set([''.join(map(str, s)) for s in set(P(card, k))])))