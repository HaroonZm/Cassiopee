while True:
    line = input()
    if line == "0 0 0":
        break
    n, k, m = map(int, line.split())
    stones = list(range(1, n + 1))
    # trouver l'index de la pierre m
    idx = stones.index(m)
    while len(stones) > 1:
        stones.pop(idx)
        # hop k-1 fois en comptant uniquement les pierres restantes
        idx = (idx + (k - 1)) % len(stones)
    print(stones[0])