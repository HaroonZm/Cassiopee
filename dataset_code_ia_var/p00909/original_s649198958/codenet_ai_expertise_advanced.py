import sys
import random
from collections import defaultdict
from functools import partial

# Constantes globales optimisées
sys.setrecursionlimit(1 << 25)
INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
DIRS_4 = [(-1,0),(0,1),(1,0),(0,-1)]
DIRS_8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Fonctions d'entrée efficaces
input = sys.stdin.readline
parse_ints = lambda: list(map(int, input().split()))
parse_ints0 = lambda: [x - 1 for x in map(int, input().split())]
parse_floats = lambda: list(map(float, input().split()))
raw_strings = lambda: input().split()
get_int = lambda: int(input())
get_float = lambda: float(input())
get_string = lambda: input().rstrip()
pflush = partial(print, flush=True)

class UnionFind:
    __slots__ = ['parent']
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        px = self.parent[x]
        if px < 0:
            return x
        self.parent[x] = self.find(px)
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root
        return True

    def groups(self):
        return [(i, -s) for i, s in enumerate(self.parent) if s < 0]


def main():
    random.seed(42)
    answers = []
    while True:
        n, m = parse_ints()
        if n == 0 and m == 0:
            break
        queries = [raw_strings() for _ in range(m)]
        d = defaultdict(lambda: defaultdict(int))
        for i in range(n + 1):
            d[i][i] = random.randint(1, 99)
        uf = UnionFind(n + 1)
        for q in queries:
            if q[0] == '!':
                a, b, w = map(int, q[1:])
                root_a = uf.find(a)
                root_b = uf.find(b)
                if root_a == root_b:
                    continue
                uf.union(a, b)
                new_root = uf.find(a)
                if new_root == root_a:
                    shift = w + (d[root_a][a] - d[root_b][b])
                    for k, v in d[root_b].items():
                        d[root_a][k] = v + shift
                else:
                    shift = (d[root_a][a] - d[root_b][b]) + w
                    for k, v in d[root_a].items():
                        d[root_b][k] = v - shift
            else:
                a, b = map(int, q[1:])
                if uf.find(a) != uf.find(b):
                    answers.append('UNKNOWN')
                else:
                    root = uf.find(a)
                    answers.append(d[root][b] - d[root][a])
    return '\n'.join(map(str, answers))

if __name__ == "__main__":
    print(main())