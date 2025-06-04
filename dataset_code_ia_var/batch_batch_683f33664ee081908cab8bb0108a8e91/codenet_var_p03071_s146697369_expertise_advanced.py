import sys
from functools import lru_cache, partial
from operator import itemgetter
from statistics import mean
from math import gcd as math_gcd, ceil as math_ceil

class IP:
    __slots__ = ('input',)
    def __init__(self):
        self.input = sys.stdin.readline

    def I(self) -> int:
        return int(self.input())

    def S(self) -> str:
        return self.input().rstrip('\n')

    def IL(self) -> list[int]:
        return list(map(int, self.input().split()))

    def SL(self) -> list[str]:
        return self.input().split()

    def ILS(self, n: int) -> list[int]:
        return [int(self.input()) for _ in range(n)]

    def SLS(self, n: int) -> list[str]:
        return [self.input().rstrip('\n') for _ in range(n)]

    def SILS(self, n: int) -> list[list[int]]:
        return [self.IL() for _ in range(n)]

    def SSLS(self, n: int) -> list[list[str]]:
        return [self.SL() for _ in range(n)]

class Idea:
    __slots__ = ()
    @staticmethod
    def HF(p):
        # 半分全列挙: 和の組み合わせを求めて重複なし・ソート
        from itertools import combinations_with_replacement
        return sorted(set(sum(x) for x in combinations_with_replacement(p, 2)))

    @staticmethod
    def Bfs2(a):
        # bit全探索：bit列(16桁), その総和をリストで返す
        N = len(a)
        fmt = f'0{max(16, N)}b'
        results = [(format(mask, fmt), sum(a[j] for j in range(N) if (mask>>j)&1)) for mask in range(1<<N)]
        results.sort(key=itemgetter(1))
        return [b for b, _ in results], [v for _, v in results]

    @staticmethod
    def S(s, r=0, m=-1):
        s.sort(reverse=bool(r), key=None if m == -1 else itemgetter(m))

    @staticmethod
    def bit_n(a, b):
        return (a >> b) & 1 > 0

    @staticmethod
    def bit_o(a, b):
        return ((a >> b) & 1) == 1

    @staticmethod
    def ceil(x, y):
        return math_ceil(x / y)

    @staticmethod
    def ave(a):
        return mean(a)

    @staticmethod
    @lru_cache(maxsize=None)
    def gcd(x, y):
        return math_gcd(x, y)

def main():
    r, e, p = range, enumerate, print
    ip = IP()
    id = Idea()
    mod = 10**9 + 7

    a, b = ip.IL()
    # 2回取り出す最大値計算の最短化
    ans = max(a, b)
    ans += max(a-1, b-1)
    p(ans)

main()