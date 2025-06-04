from __future__ import division, print_function
from sys import stdin, maxint

def read_num():
    return int(stdin.readline())

def read_edges():
    return [int(s) for s in stdin.readline().split()[1:]]

def iter_pairs(vals):
    it = iter(vals)
    return [(next(it), next(it)) for _ in xrange(next(it))]

def read_graph(num):
    L = []
    for _ in xrange(num):
        vals = read_edges()
        edges = iter_pairs(vals)
        L.append(edges)
    return L

def init_weights(num):
    weight = [maxint] * num
    weight[0] = 0
    return weight

def init_unvisited(num):
    return set(xrange(1, num))

def update_weights(L, weight, V, index):
    for v, cost in L[index]:
        if v in V:
            weight[v] = min(weight[v], cost + weight[index])

def select_min_index(V, weight):
    return min(V, key=lambda i: weight[i])

def print_weights(weight):
    for i, d in enumerate(weight):
        print(i, d)

def solve():
    num = read_num()
    L = read_graph(num)
    weight = init_weights(num)
    V = init_unvisited(num)
    index = 0

    while continue_loop(V):
        process_iteration(L, weight, V, index)
        index = update_index(V, weight)

    print_weights(weight)

def process_iteration(L, weight, V, index):
    update_weights(L, weight, V, index)

def update_index(V, weight):
    idx = select_min_index(V, weight)
    V.remove(idx)
    return idx

def continue_loop(V):
    return bool(V)

def main():
    solve()

main()