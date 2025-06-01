from sys import setrecursionlimit
setrecursionlimit(10**7)

from functools import lru_cache

# Predefined permutations for operations
_ops = {
    1: (0,1,2,3,4,5,21,22,23,11,10,9,17,13,14,15,16,12,18,19,20,6,7,8,24,25,26,27,28,29),
    2: (27,28,29,3,4,5,6,7,8,9,10,11,12,13,15,14,16,17,20,19,18,21,22,23,24,25,26,0,1,2),
    3: (23,1,2,26,4,5,29,7,8,20,10,11,12,13,14,17,16,15,18,19,9,21,22,0,24,25,3,27,28,6),
    4: (0,1,21,3,4,24,6,7,27,9,10,18,14,13,12,15,16,17,11,19,20,2,22,23,5,25,26,8,28,29),
}

_valid_patterns = {
    (0,1,3,5,4,2),
    (0,3,5,4,1,2),
    (0,5,4,1,3,2),
    (0,4,1,3,5,2),
    (2,1,5,3,4,0),
    (2,5,3,4,1,0),
    (2,3,4,1,5,0),
    (2,4,1,5,3,0),
}

def op(p, i):
    permutation = _ops[i]
    return tuple(p[idx] for idx in permutation)

def valid(p):
    # Function to test if all elements in p[start:end] are same as p[start]
    def all_same(start, end):
        v = p[start]
        return all(p[k] == v for k in range(start, end))
    
    if not all_same(0,9):           # positions 0 to 8
        return False
    if not all_same(21,30):         # positions 21 to 29
        return False
    if not all_same(9,12):          # positions 9 to 11
        return False
    if not all_same(13,15):         # positions 13 to 14
        return False
    if not all_same(16,18):         # positions 16 to 17
        return False
    if not all_same(19,21):         # positions 19 to 20
        return False

    q = (p[0], p[9], p[12], p[15], p[18], p[21])
    return q in _valid_patterns

@lru_cache(None)
def solve(n, p, i):
    if n > 9:
        return float('inf')
    if valid(p):
        return n
    res = float('inf')
    for j in range(1,5):
        if i != j:
            res = min(res, solve(n+1, op(p,j), j))
    return res

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        p = tuple(int(x)-1 for x in input().split())
        if valid(p):
            print(0)
            continue
        ans = float('inf')
        for i in range(1,5):
            ans = min(ans, solve(1, op(p,i), i))
        print(ans)

if __name__ == '__main__':
    main()