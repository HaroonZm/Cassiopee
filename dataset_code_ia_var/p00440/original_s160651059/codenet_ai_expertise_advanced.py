import sys
from itertools import islice, pairwise
from typing import List, Any
from functools import cache

sys.setrecursionlimit(100000)
input = sys.stdin.readline

INF = float('inf')

@cache
def sgn(n: int) -> int:
    return (n > 0) - (n < 0)

def get_int() -> int:
    return int(input())

def get_float() -> float:
    return float(input())

def get_str() -> str:
    return input().strip()

def get_li() -> List[int]:
    return list(map(int, input().split()))

def get_lf() -> List[float]:
    return list(map(float, input().split()))

def get_lc() -> List[str]:
    return list(input().strip())

def get_data(n: int, types: List[Any], sep=None):
    converter = types[0]
    if len(types) == 1:
        return [converter(input()) for _ in range(n)]
    return [tuple(t(x) for t, x in zip(types, line.split(sep=sep))) for line in islice(sys.stdin, n)]

def set_inputs():
    N, K, C = [], [], []
    for line in sys.stdin:
        n, k = map(int, line.strip().split())
        if n == k == 0: break
        N.append(n)
        K.append(k)
        c_list = []
        for _ in range(k):
            c_list.append(int(input()))
        C.append(c_list)
    return N, K, C

def find_max_sequence(c: List[int]) -> int:
    c.sort()
    if not c: return 0
    if c[0] == 0:
        tmp = ans = 0
        for v1, v2 in pairwise(c):
            if v2 - v1 == 1:
                tmp += 1 * sgn(tmp if tmp else 1)
                ans = max(ans, abs(tmp))
            elif v2 - v1 == 2:
                tmp = -tmp-2 if tmp > 0 else -3
            else:
                tmp = 1
        return abs(ans+1) if ans > 0 else 0
    else:
        tmp = ans = 1
        for v1, v2 in pairwise(c):
            if v2 - v1 == 1:
                tmp += 1
                ans = max(ans, tmp)
            else:
                tmp = 1
        return ans

def main():
    N, K, C = set_inputs()
    for c in C:
        print(find_max_sequence(c))

if __name__ == '__main__':
    main()