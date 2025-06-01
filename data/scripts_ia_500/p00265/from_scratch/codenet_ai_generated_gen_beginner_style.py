N, Q = map(int, input().split())
cards = list(map(int, input().split()))
queries = [int(input()) for _ in range(Q)]

for q in queries:
    max_mod = 0
    for c in cards:
        r = c % q
        if r > max_mod:
            max_mod = r
    print(max_mod)