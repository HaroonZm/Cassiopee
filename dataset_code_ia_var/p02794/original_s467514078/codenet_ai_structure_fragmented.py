def read_n():
    return int(input())

def initialize_ab(n):
    return {i: [] for i in range(n)}

def read_edge_input():
    return [int(i) - 1 for i in input().split()]

def add_edge(ab, a, b, idx):
    ab[a].append((b, idx))
    ab[b].append((a, idx))

def build_graph(n):
    ab = initialize_ab(n)
    for j in range(n - 1):
        a, b = read_edge_input()
        add_edge(ab, a, b, j)
    return ab

def dfs_helper(a, b, d, ab, c):
    if a == b:
        return d
    for i in ab[a]:
        if i[0] == c:
            continue
        e = dfs_helper(i[0], b, d + [i[1]], ab, a)
        if len(e) != 0:
            return set(e)
    return set()

def dfs(a, b, ab):
    return dfs_helper(a, b, [], ab, -1)

def read_m():
    return int(input())

def read_query():
    return [int(i) - 1 for i in input().split()]

def process_queries(m, ab):
    ms = []
    for _ in range(m):
        u, p = read_query()
        ms.append(dfs(u, p, ab))
    return ms

def count_bits(i, m):
    return bin(i).count('1')

def combine_sets(i, m, ms):
    a = set()
    for j in range(m):
        if (i >> j) & 1:
            a |= ms[j]
    return a

def process_mask(i, m, ms, n):
    k = 0
    a = set()
    for j in range(m):
        if (i >> j) & 1 == 1:
            k += 1
            a |= ms[j]
    if k % 2 == 1:
        return 2 ** (n - 1 - len(a))
    elif k != 0:
        return -2 ** (n - 1 - len(a))
    return 0

def process_all_masks(m, n, ms):
    ans = 0
    for i in range(1 << m):
        ans += process_mask(i, m, ms, n)
    return ans

def compute_answer(n, ans):
    return 2 ** (n - 1) - ans

def main():
    n = read_n()
    ab = build_graph(n)
    m = read_m()
    ms = process_queries(m, ab)
    ans = process_all_masks(m, n, ms)
    print(compute_answer(n, ans))

main()