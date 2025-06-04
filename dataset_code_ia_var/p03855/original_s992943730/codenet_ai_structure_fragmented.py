import sys
from collections import defaultdict

def get_input():
    return sys.stdin.read

def get_readline():
    return sys.stdin.readline

def get_readlines():
    return sys.stdin.readlines

def create_union_find(n):
    return UnionFind(n)

def union_pairs(uf, pairs):
    for p, q in pairs:
        uf.union(p-1, q-1)

def input_nkl():
    return map(int, input().split())

def parse_pairs(count, readline_fn):
    pairs = []
    for _ in range(count):
        p, q = map(int, readline_fn().split())
        pairs.append((p, q))
    return pairs

def get_group_keys(uf1, uf2, n):
    group_keys = []
    for i in range(n):
        group_keys.append((uf1.find(i), uf2.find(i)))
    return group_keys

def count_groups(group_keys):
    dd = defaultdict(int)
    for g in group_keys:
        dd[g] += 1
    return dd

def group_counts_for_all(group_keys, group_count_dict, n):
    ans = []
    for i in range(n):
        ans.append(group_count_dict[group_keys[i]])
    return ans

def output_answer(ans):
    print(' '.join(map(str, ans)))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        return self._find_rec(x)

    def _find_rec(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self._find_rec(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        self._union_by_rank(x, y)

    def _union_by_rank(self, x, y):
        x = self._find_rec(x)
        y = self._find_rec(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return self._get_size(x)

    def _get_size(self, x):
        return -self.parents[self._find_rec(x)]

    def same(self, x, y):
        return self._find_rec(x) == self._find_rec(y)

    def members(self, x):
        return self._get_members(x)

    def _get_members(self, x):
        root = self._find_rec(x)
        return [i for i in range(self.n) if self._find_rec(i) == root]

    def roots(self):
        return self._get_roots()

    def _get_roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self._get_roots())

    def all_group_members(self):
        return {r: self._get_members(r) for r in self._get_roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self._get_members(r)) for r in self._get_roots())

def main():
    N, K, L = input_nkl()
    read = get_input()
    readline = get_readline()
    ufl = create_union_find(N)
    uft = create_union_find(N)
    road_pairs = parse_pairs(K, readline)
    train_pairs = parse_pairs(L, readline)
    union_pairs(ufl, road_pairs)
    union_pairs(uft, train_pairs)
    group_keys = get_group_keys(ufl, uft, N)
    group_count_dict = count_groups(group_keys)
    ans = group_counts_for_all(group_keys, group_count_dict, N)
    output_answer(ans)

if __name__ == "__main__":
    main()