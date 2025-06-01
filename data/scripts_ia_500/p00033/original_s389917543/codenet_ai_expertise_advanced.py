from sys import stdin
from functools import lru_cache

def is_sorted(seq):
    return all(x <= y for x, y in zip(seq, seq[1:]))

@lru_cache(None)
def dfs(idx, b, c, a):
    if len(b) + len(c) == 10:
        return is_sorted(b) and is_sorted(c)
    return (dfs(idx + 1, b + (a[idx],), c, a) or
            dfs(idx + 1, b, c + (a[idx],), a))

def main():
    input_data = iter(stdin.read().strip().split('\n'))
    n = int(next(input_data))
    for _ in range(n):
        a = tuple(map(int, next(input_data).split()))
        print('YES' if dfs(0, (), (), a) else 'NO')

if __name__ == '__main__':
    main()