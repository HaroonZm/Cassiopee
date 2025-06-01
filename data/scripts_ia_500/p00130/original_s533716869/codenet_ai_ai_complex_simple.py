import sys
from collections import deque as __dq
import builtins as __b

__input = sys.stdin.readline

def __bfs(start, accum, graph_out, indegs, marks):
    q = __dq()
    q.append(start)
    marks[start] = True
    while q:
        curr = q.popleft()
        accum.append(curr)
        list(map(lambda nxt: (indegs.__setitem__(nxt, indegs[nxt] - 1), (q.append(nxt), marks.__setitem__(nxt, True)) if (indegs[nxt] == 0 and not marks[nxt]) else None)[1] if indegs[nxt] == 0 and not marks[nxt] else None, graph_out[curr]))

def __solve(V, indegs, graph_out):
    res = []
    marks = [False] * V
    list(map(lambda u: __bfs(u, res, graph_out, indegs, marks) if indegs[u]==0 and not marks[u] else None, range(V)))
    return res

def __decode(S):
    acc_edges = set()
    acc_chars = set()
    ls = len(S)
    __zipper = lambda: ((S[i], S[i+3]) for i in range(ls) if 'a' <= S[i] <= 'z')
    for i in range(ls):
        try:
            if not ('a' <= S[i] <= 'z'): continue
            s = S[i]
            t = S[i+3]
            acc_chars.update((s,t))
            acc_edges.add((s,t) if S[i+1] == '-' else (t,s))
        except IndexError:
            break
    return acc_edges, acc_chars

def main(args):
    n = int(__input())
    for _ in range(n):
        S = __input().strip()
        if len(S) < 4:
            print(S)
            continue
        e_s, cs = __decode(S)
        mapping = dict(zip(cs, range(len(cs))))
        rev_map = dict(zip(mapping.values(), mapping.keys()))
        edges = list(map(lambda x: [mapping[x[0]], mapping[x[1]]], e_s))
        V = len(cs)
        indegs = [0]*V
        graph_out = [[] for _ in range(V)]
        for s,t in edges:
            graph_out[s].append(t)
            indegs[t] +=1
        res = __solve(V, indegs, graph_out)
        print(''.join(map(rev_map.get,res)))

if __name__ == '__main__':
    main(sys.argv[1:])