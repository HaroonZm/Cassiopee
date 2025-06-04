from itertools import cycle, islice

def josephus_game():
    import sys
    for line in sys.stdin:
        n, k, m = map(int, line.split())
        if not (n or k or m):
            break
        stones = list(range(1, n + 1))
        idx = (m - 1) % n
        step = k - 1
        while len(stones) > 1:
            stones.pop(idx)
            idx = (idx + step) % len(stones)
        print(stones[0])

josephus_game()