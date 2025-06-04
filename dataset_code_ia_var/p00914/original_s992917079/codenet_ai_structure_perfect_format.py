import itertools

while True:
    n, k, s = map(int, input().split())
    if n == 0:
        break
    print(
        sum(
            1
            if sum(comb) == s
            else 0
            for comb in itertools.combinations(range(1, n + 1), k)
        )
    )