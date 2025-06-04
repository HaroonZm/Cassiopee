from functools import reduce
from collections import defaultdict

def add_edge(node, adj_lst, adj_rev, s1, s2):
    # Trouver l'indice de divergence par générateur, version optimisée
    ind = next((i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2), min(len(s1), len(s2)))
    if ind == min(len(s1), len(s2)):
        return len(s1) > len(s2)
    c1, c2 = ord(s1[ind]) - 97, ord(s2[ind]) - 97
    adj_lst[c1].add(c2)
    adj_rev[c2].add(c1)
    node |= {c1, c2}
    return False

def detect_cycle(adj_lst, nodes):
    visited = [0] * 26
    def dfs(n):
        if visited[n] == 2: return True
        if visited[n] == 1: return False
        visited[n] = 2
        for to in adj_lst[n]:
            if dfs(to): return True
        visited[n] = 1
        return False
    return any(dfs(n) for n in nodes)

def main():
    while (n := int(input())) != 0:
        lst = [input() for _ in range(n)]
        node = set()
        adj_lst = [set() for _ in range(26)]
        adj_rev = [set() for _ in range(26)]
        blank_flag = any(add_edge(node, adj_lst, adj_rev, lst[i], lst[j]) 
                         for i in range(n) for j in range(i + 1, n))
        cycle_flag = detect_cycle(adj_lst, node)
        print("no" if cycle_flag or blank_flag else "yes")

main()