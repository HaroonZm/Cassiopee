from sys import stdin
from functools import reduce, partial
from itertools import chain, count, compress, islice, groupby, filterfalse, starmap
from collections import defaultdict, deque, namedtuple
from operator import itemgetter, attrgetter
import heapq

def tree_walk_1(start, parent=None):
    def walk(s, p):
        list(map(lambda z: (P.__setitem__(z[0], (s, z[1])),
                            C[s].append((z[0], z[1])),
                            z[0] != p and walk(z[0], s))[2],
                 filter(lambda u: u[0] != p, adj[s])))
    walk(start, parent)

def tree_walk_2(start):
    global time
    stack = []
    stack.append(start)
    while stack:
        s = stack.pop()
        if notVisited[s]:
            notVisited[s] = False
            stack.extend([c for c, _ in C[s] if notVisited[c]])
            time += sum(2 * t for c, t in C[s] if notVisited[c])
            p, t2 = P[s]
            if notVisited[p]:
                time += t2
                stack.append(p)

f_i = stdin
for _ in count():
    N = int(f_i.readline())
    if N == 0:
        break

    adj = [[] for _ in range(N)]
    trash = list(starmap(lambda a, b, t: (
        adj.__getitem__(a-1).append((b-1, t)), 
        adj.__getitem__(b-1).append((a-1, t))
    ), (map(int, f_i.readline().split()) for _ in range(N-1))))
    
    # leaf cutting
    leaves = list(filter(lambda x: len(adj[x]) == 1, range(1, N)))
    _ = list(map(lambda l: (lambda pair: adj[pair[0]].remove((l, pair[1])))(adj[l].pop()), leaves))
    
    rc = list(filter(lambda x: len(adj[x]) == 1, range(1, N)))
    if not rc:
        print(0)
        continue

    def simulate_tree(r):
        global time, P, C, notVisited
        P = [None]*N
        P[r] = (r, 0)
        C = [[] for _ in range(N)]
        tree_walk_1(r)
        time = 0
        notVisited = [True]*N
        tree_walk_2(0)
        return time

    print(min(starmap(simulate_tree, ((r,) for r in rc))))