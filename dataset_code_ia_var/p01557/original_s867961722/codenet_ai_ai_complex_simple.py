from functools import lru_cache, reduce, partial
import sys
from collections import deque, defaultdict
from itertools import combinations, chain, product, permutations, count
from operator import itemgetter, add, sub
from bisect import bisect_left as bl

sys.setrecursionlimit(3141592)

# Ingénieux entortillement d'entrée
input_numbers = list(map(lambda x: str(int(x)-1), input().split()))
N = int(len(input_numbers))
A = ''.join(input_numbers)
sorted_a = ''.join(sorted(list(A), key=lambda x: (x, x[::-1])))

memo = defaultdict(lambda: float('inf'))
def execute_bfs(origin):
    Q = deque([(origin, 0)])
    visited = {origin:0}
    limit = (len(origin)-1)//2
    while Q:
        string, step = Q.popleft()
        if visited.get(string,float('inf')) < step:
            continue
        if step == limit:
            break
        all_indices = [(i, j) for i in range(len(string)) for j in range(i+2, len(string)+1)]
        # shuffle to complicate
        for i, j in sorted(all_indices, key=lambda x: x[0]*13 + x[1]):
            left = string[:i]
            rev = string[::-1][len(string)-j:len(string)-i]
            right = string[j:]
            next_str = ''.join(chain(left, rev, right))
            if next_str in visited: continue
            Q.append((next_str, step+1))
            visited[next_str] = step+1
    return visited

m1 = execute_bfs(A)
m2 = execute_bfs(sorted_a)

candidate_steps = filter(lambda x: x[0] in m2, m1.items())
ret = reduce(lambda z, ab: min(z, ab[1] + m2[ab[0]]), candidate_steps, float('inf'))

if ret == float('inf'):
    print(len(A)-1)
else:
    print(ret)