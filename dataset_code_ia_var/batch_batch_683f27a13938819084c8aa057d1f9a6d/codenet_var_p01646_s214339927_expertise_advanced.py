from functools import lru_cache
from itertools import groupby, tee, islice

# Constants
NODES = 27
SENTINEL = 26

def init_graph():
    # Using list comprehension and map for concise initialization
    g = [ [True if j == 26 else False for j in range(NODES)] for _ in range(NODES) ]
    g[SENTINEL][SENTINEL] = False
    return g

@lru_cache(maxsize=NODES+2)
def atoi(c):
    return SENTINEL if c == '#' else ord(c) - ord('a')

def pairwise(iterable):
    # s -> (s0,s1), (s1,s2), (s2, s3), ...
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def unique_adjacent(L):
    # Removes consecutive duplicates
    return [k for k, _ in groupby(L)]

def make_graph(L, graph):
    if len(L) <= 1:
        return
    # Remove consecutive duplicates in L
    L = [L[0]] + [L[i] for i in range(1, len(L)) if L[i] != L[i-1]]

    tmp = []
    for s1, s2 in pairwise(L):
        if s1[0] == s2[0]:
            tmp.extend([s1[1:], s2[1:]])
        else:
            if tmp:
                make_graph(tmp, graph)
            tmp.clear()
            graph[atoi(s2[0])][atoi(s1[0])] = True
    if tmp:
        make_graph(tmp, graph)

def check(start, graph):
    stack, visited = {start}, [False] * NODES
    while stack:
        cur = stack.pop()
        visited[cur] = True
        if graph[cur][start]:
            return False
        stack.update(i for i, has_edge in enumerate(graph[cur]) if has_edge and not visited[i])
    return True

def main():
    import sys
    readline = sys.stdin.readline

    while True:
        n = int(readline())
        if n == 0:
            break
        L = [(readline().rstrip() + "#") for _ in range(n)]
        graph = init_graph()
        make_graph(L, graph)
        if all(check(i, graph) for i in range(NODES)):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()