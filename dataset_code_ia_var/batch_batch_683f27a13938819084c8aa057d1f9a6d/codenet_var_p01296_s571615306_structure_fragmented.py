from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    return list(sys.stdin.readline())[:-1]

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

move = [(0,1), (1,0)]

def get_input_and_initialize(n):
    f = defaultdict(lambda: 0)
    v = defaultdict(list)
    l = []
    input_data = []
    for _ in range(n):
        line = sys.stdin.readline().split()
        a, b, dir = int(line[0]), int(line[1]), line[2]
        input_data.append((a, b, dir))
    return input_data, f, v, l

def convert_dir_to_int(dir):
    return 0 if dir == "x" else 1

def add_edges_and_fill_structs(input_data, f, v, l):
    for a, b, dir in input_data:
        f[(a, b)] = 1
        dir_int = convert_dir_to_int(dir)
        na, nb = a + 1 - dir_int, b + dir_int
        f[(na, nb)] = 1
        l.append((a, b, na, nb))
        l.append((na, nb, a, b))
        add_primary_edges(a, b, na, nb, v)
    return

def add_primary_edges(a, b, na, nb, v):
    v[(a, b)].append(((na, nb), 1))
    v[(na, nb)].append(((a, b), 1))

def add_secondary_edges(l, move, f, v):
    for a, b, c, d in l:
        for dx, dy in move:
            na, nb = a + dx, b + dy
            if f[(na, nb)] and (c, d) != (na, nb):
                v[(a, b)].append(((na, nb), 0))
                v[(na, nb)].append(((a, b), 0))
    return

def try_bfs_from_node(a, b, v, bfs):
    q = deque()
    q.append((a, b))
    bfs[(a, b)] = 0
    while q:
        x, y = q.popleft()
        process_node_neighbors(x, y, v, bfs, q)
    return

def process_node_neighbors(x, y, v, bfs, q):
    for node, k in v[(x, y)]:
        nx, ny = node
        nb = 1 - bfs[(x, y)] if k else bfs[(x, y)]
        if bfs[(nx, ny)] >= 0:
            if bfs[(nx, ny)] != nb:
                print("No")
                raise BFSConflictException()
        else:
            bfs[(nx, ny)] = nb
            q.append((nx, ny))
    return

class BFSConflictException(Exception):
    pass

def full_bfs(l, v):
    bfs = defaultdict(lambda: -1)
    try:
        for a, b, c, d in l:
            if bfs[(a, b)] < 0:
                try_bfs_from_node(a, b, v, bfs)
    except BFSConflictException:
        return False
    return True

def solve(n):
    input_data, f, v, l = get_input_and_initialize(n)
    add_edges_and_fill_structs(input_data, f, v, l)
    add_secondary_edges(l, move, f, v)
    result = full_bfs(l, v)
    print("Yes" if result else "No")
    return

def read_and_process():
    while True:
        n = I()
        if n == 0:
            break
        solve(n)

if __name__ == "__main__":
    read_and_process()