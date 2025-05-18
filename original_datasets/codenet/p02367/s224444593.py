from typing import List
from typing import Tuple
from functools import cmp_to_key
import sys

sys.setrecursionlimit(100000)

def find_bridges(adj, n) -> List[Tuple[int, int]]:
    mark = [False for _ in range(n)] 
    edges = []
    low_link = [None for _ in range(n)]
    id = [0]

    for v in range(n):
        if not mark[v]:
            ____find_bridges(v, -1, adj, id, low_link, mark, edges)
    return edges

def ____find_bridges(node: int, parent: int, adj, id: List[int], low_link: List[int], mark: List[bool], edges):

    mark[node] = True
    low_link[node] = id[0]
    node_id = id[0]

    for v in adj[node]:
        if v == parent: continue
        if not mark[v]:
            id[0] += 1
            ____find_bridges(v, node, adj, id, low_link, mark, edges)
        low_link[node] = min(low_link[node], low_link[v])
        if low_link[v] > node_id:
            edges.append([node, v])

def read() -> Tuple[List, int]:

    info = [int(e) for e in input().split()]
    n, e = info[0], info[1]
    adj = [[] for _ in range(n)]
    for _ in range(e):
        edge = [int(i) for i in input().split()]
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    
    return adj, n

def custom_cmp(edgeA, edgeB):
    if edgeA[0] == edgeB[0]:
        return edgeA[1] - edgeB[1]
    
    return edgeA[0] - edgeB[0]

def process_output(edges: List[List[int]]) -> List[List[int]]:
    for edge in edges:
        edge.sort()
    n_edges = list(sorted(edges, key=cmp_to_key(custom_cmp)))
    return n_edges

def show(edges):
    for edge in edges:
        print('%d %d' % (edge[0], edge[1]))

adj, n = read()
edges = find_bridges(adj, n)
n_edges = process_output(edges)
show(n_edges)