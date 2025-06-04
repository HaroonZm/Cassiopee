import sys
from collections import Counter
from itertools import islice, combinations_with_replacement
from functools import partial

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_str_list():
    return sys.stdin.readline().split()

def read_str():
    return sys.stdin.readline().strip()

def vanish(p, details=False):
    while p:
        if details:
            print(p)
        n = len(p)
        p = [x for x in p if x != n]
        if len(p) == n:
            return False
    return True

def expand_check(n):
    # Efficiently generate all non-decreasing sequences of length n in [1, n]
    return (list(seq) for k in range(3, n + 1) for seq in combinations_with_replacement(range(1, n + 1), k))

def check(n):
    # Cleaned up and generalized version
    for k in range(3, n + 1):
        for seq in combinations_with_replacement(range(1, n + 1), k):
            if vanish(seq):
                print(list(seq))

def update_coverage(a, c, n):
    covered = Counter({i: 0 for i in range(n)})
    for val, cnt in c.items():
        for pos in range(val - cnt, val):
            if 0 <= pos < n:
                covered[pos] += 1
    return covered

def solve():
    n, m = read_int_list()
    a = read_int_list()
    p = [tuple(read_int_list()) for _ in range(m)]
    c = Counter(a)
    covered = Counter({i: 0 for i in range(n)})
    for val, cnt in c.items():
        for j in range(val - cnt, val):
            if 0 <= j < n:
                covered[j] += 1
    uncovered_cnt = sum(1 for v in covered.values() if v == 0)
    res = []
    for x, y in p:
        x -= 1
        old_val = a[x]
        # Remove effect of old value
        old_idx = old_val - c[old_val]
        if 0 <= old_idx < n:
            covered[old_idx] -= 1
            if covered[old_idx] == 0:
                uncovered_cnt += 1
        c[old_val] -= 1
        # Update to new value
        a[x] = y
        c[y] += 1
        new_idx = y - c[y]
        if 0 <= new_idx < n:
            if covered[new_idx] == 0:
                uncovered_cnt -= 1
            covered[new_idx] += 1
        res.append(uncovered_cnt)
    return '\n'.join(map(str, res))

def main():
    print(solve())

if __name__ == '__main__':
    main()