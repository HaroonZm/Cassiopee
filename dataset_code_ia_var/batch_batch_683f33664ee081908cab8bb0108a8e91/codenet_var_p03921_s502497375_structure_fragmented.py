import sys, copy, math, heapq, itertools as it, fractions, re, bisect, collections as coll

def create_rank_list(size):
    return [0] * size

def create_parent_list(size):
    return list(range(size))

def initialize_group_number(size):
    return size

def find_root(uf, x):
    if x == uf.par[x]:
        return x
    uf.par[x] = find_root(uf, uf.par[x])
    return uf.par[x]

def are_same_group(uf, x, y):
    return find_root(uf, x) == find_root(uf, y)

def decrease_group_number(uf):
    uf.g_num -= 1

def join_groups(uf, x, y):
    x_root = find_root(uf, x)
    y_root = find_root(uf, y)
    if x_root == y_root:
        return
    decrease_group_number(uf)
    if uf.rank[x_root] > uf.rank[y_root]:
        uf.par[y_root] = x_root
    else:
        uf.par[x_root] = y_root
        if uf.rank[x_root] == uf.rank[y_root]:
            uf.rank[y_root] += 1

def get_group_count(uf):
    return uf.g_num

class UnionFind:
    def __init__(self, size):
        self.rank = create_rank_list(size)
        self.par = create_parent_list(size)
        self.g_num = initialize_group_number(size)
    def find(self, x):
        return find_root(self, x)
    def same(self, x, y):
        return are_same_group(self, x, y)
    def unite(self, x, y):
        join_groups(self, x, y)
    def group_num(self):
        return get_group_count(self)

def get_input_values():
    return map(int, raw_input().split())

def get_input_matrix(rows):
    return [get_input_values() for _ in xrange(rows)]

def create_initial_sp(m):
    return [-1] * m

def initialize_union_find(n):
    return UnionFind(n)

def process_language_input(L, N, M):
    sp = create_initial_sp(M)
    uf = initialize_union_find(N)
    for i in range(N):
        k = get_language_count(L, i)
        for j in get_language_indices(k):
            lang_idx = get_language_index(L, i, j)
            sp_elem = sp[lang_idx]
            if sp_elem == -1:
                set_sp_entry(sp, lang_idx, i)
            else:
                unite_speakers(uf, sp_elem, i)
    return uf

def get_language_count(L, i):
    return L[i][0]

def get_language_indices(k):
    return range(1, k + 1)

def get_language_index(L, i, j):
    return L[i][j] - 1

def set_sp_entry(sp, lang_idx, i):
    sp[lang_idx] = i

def unite_speakers(uf, a, b):
    uf.unite(a, b)

def print_result(uf):
    if check_all_connected(uf):
        print "YES"
    else:
        print "NO"

def check_all_connected(uf):
    return uf.group_num() == 1

def main():
    N, M = get_input_values()
    L = get_input_matrix(N)
    uf = process_language_input(L, N, M)
    print_result(uf)

main()