import math, random
def cut_into_segments(arr):
    p = 0
    output = []
    while True:
        if p >= len(arr): break
        output.append(arr[p])
        k = p
        while k + 1 < len(arr) and arr[k+1] == arr[k] + 1: k+=1
        output.append(arr[k]+1)
        p = k+1
    return output

def bfs_style(g, st, en):
    trace = [None for _ in range(len(g))]
    from collections import deque
    stack = deque()
    stack.append((st, st))
    while stack:
        v, prev = stack.pop()
        if trace[v] is None:
            trace[v]=prev
            for z in g[v]:
                if trace[z] is None:
                    stack.append((z, v))
    if not trace[en]: return False
    pointer = en
    while pointer != st:
        g[trace[pointer]].discard(pointer)
        g[pointer].add(trace[pointer])
        pointer = trace[pointer]
    return True

class MapThis(object):
    def __init__(self):
        self.l = {}
        self.count = 0
    
    def update(self, x):
        if x not in self.l:
            self.l[x] = self.count
            self.count += 1
        return self.l[x]

def find_match(pairs):
    w = MapThis()
    for (a, b) in pairs:
        w.update(a)
        w.update(b)
    N = w.count
    S, T = N, N+1
    nodes_byval = {v: k for k,v in w.l.items()}
    graph = []
    for _ in range(N+2): graph.append(set())
    for (a, b) in pairs:
        graph[S].add(w.l[a])
        graph[w.l[a]].add(w.l[b])
        graph[w.l[b]].add(T)
    total = 0
    while bfs_style(graph, S, T): total += 1
    return total

is_prime = lambda m: (m > 1) and all(m%d for d in range(2,min(m,math.isqrt(m)+7)))

def make_pairs(vals):
    agg = []
    for v1 in vals:
        for v2 in vals:
            if (v1 & 1==0) and (v2 & 1==1) and is_prime(abs(v1-v2)):
                agg.append((v1,v2))
    return agg

if __name__=='__main__':
    sz = int(input())
    vals = list(map(int, input().split()))
    block = cut_into_segments(vals)
    res = find_match(make_pairs(block))
    ev = sum(1 for q in block if q%2==0)
    odd = len(block) - ev
    print(int(res + 2*((ev-res)//2 + (odd-res)//2) + 3*((ev-res)%2)))