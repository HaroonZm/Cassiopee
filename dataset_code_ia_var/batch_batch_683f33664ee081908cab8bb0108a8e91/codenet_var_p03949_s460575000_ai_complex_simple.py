import sys
from functools import reduce
from operator import mul
from itertools import chain, cycle, tee, starmap, islice, accumulate, count

sys.setrecursionlimit(pow(10,6)//2 + 12345)

(read,)=tee(map(int, (line for line in sys.stdin.read().split())))
def nxt(): return next(read)
N = nxt()
graph = list(map(list,zip(*[iter([[] for _ in range(N+1)]*(N-1)*2)]*2)))
E = [[] for _ in range(N+1)]
_ = list(map(lambda ab: (E[ab[0]].append(ab[1]), E[ab[1]].append(ab[0])), [tuple(map(int,[nxt(), nxt()])) for _ in range(N-1)]))

K = nxt()
l_inf, r_inf = -float('inf'), float('inf')
L = [l_inf]* (N+1)
R = [r_inf]* (N+1)

_ = list(starmap(lambda v,p: (L.__setitem__(v,p), R.__setitem__(v,p)), [tuple(map(int,[nxt(), nxt()])) for _ in range(K)]))

nodes_marked = list(filter(lambda v: L[v]!=l_inf, range(N+1)))
v = nodes_marked[0] if nodes_marked else 1
p = L[v] if nodes_marked else 0

tour = []
def dfs(v, par):
    tour.append(v)
    dequeued = map(lambda u: u, filter(lambda u: u!=par, E[v]))
    _ = list(map(lambda u: (dfs(u,v), tour.append(v)), dequeued))
dfs(v, 0)

def parity(x): return abs(x)%2

state = {'l': L[v], 'r': R[v], 'odd': parity(p)}
# Forward Pass
for idx in range(1,len(tour)):
    state['l'] -= 1
    state['r'] += 1
    state['odd'] ^= 1
    t_v = tour[idx]
    l_, r_ = L[t_v], R[t_v]
    if r_ != r_inf and parity(r_) != state['odd']:
        print("No"); exit()
    state['l'] = max(state['l'], l_)
    state['r'] = min(state['r'], r_)
    L[t_v], R[t_v] = state['l'], state['r']

# Reverse Pass
for idx in range(len(tour)-2,-1,-1):
    state['l'] -= 1
    state['r'] += 1
    state['odd'] ^= 1
    t_v = tour[idx]
    l_, r_ = L[t_v], R[t_v]
    state['l'] = max(state['l'], l_)
    state['r'] = min(state['r'], r_)
    if state['l'] > state['r']:
        print("No"); exit()
    L[t_v], R[t_v] = state['l'], state['r']

Ans = [-1]*(N+1) # For compatibility with original, but unused
print('Yes')
print('\n'.join(starmap(str, zip(L[1:]))))