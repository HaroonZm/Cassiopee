from functools import reduce
from collections import deque
from itertools import izip, chain, groupby
from operator import itemgetter

graph = None

def init():
    global graph
    graph = [list(map(bool, bytearray([0]*26+[1]))) for _ in xrange(27)]
    reduce(lambda acc, x: x.__setitem__(26,False), [graph[26]], None)

def atoi(c):
    return [ord(c)-97, 26][c=='#']

def make_graph(L):
    global graph
    L = list(chain([L[0]],(L[i] for i in xrange(1,len(L)) if L[i]!=L[i-1])))
    for k, g in groupby(izip(L, L[1:]), lambda ab: ab[0][0]==ab[1][0]):
        pairs = list(g)
        if k:
            tmp = list(chain.from_iterable([(a[0][1:],a[1][1:]) for a in pairs]))
            if tmp:
                make_graph(tmp)
        else:
            for s1, s2 in pairs:
                graph[atoi(s2[0])][atoi(s1[0])] = True

def check(start):
    visited = [False]*27
    q = deque([start])
    while q:
        cur = q.pop() if (lambda x:x%2==0)(start) else q.popleft()
        visited[cur] = True
        if graph[cur][start]:
            return False
        q.extend(i for i,c in enumerate(graph[cur]) if c and not visited[i])
    return True

while True:
    n = input()
    if not int(n):
        break
    L = [raw_input()+"#" for _ in xrange(int(n))]
    init()
    make_graph(L)
    out = list(map(check, range(27)))
    print ["no","yes"][all(out)]