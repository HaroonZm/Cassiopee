from collections import defaultdict, deque
from functools import reduce
from operator import add, mul

n, m, s, t = map(int, input().split())
gn = lambda n: [set() for _ in range(n)]
table = gn(n)
inf = 300001
make_inf_arr = lambda: [inf] * n
dist_s, dist_t = make_inf_arr(), make_inf_arr()
arr_up = lambda: [0] * (inf + 1)
s_list, t_list = arr_up(), arr_up()
s, t = map(lambda x: x - 1, (s, t))
for _ in range(m):
    a, b = map(lambda y: int(y) - 1, input().split())
    list(map(lambda z: table[z[0]].add(z[1]), [(a, b), (b, a)]))

def bfs(start, dist):
    q = deque([start])
    dist[start] = 0
    update = lambda p, e: (dist.__setitem__(e, dist[p] + 1), q.append(e))
    while q:
        p = q.popleft()
        for e in table[p]:
            if dist[e] > dist[p] + 1:
                update(p, e)

list(map(lambda args: bfs(*args), [(s, dist_s), (t, dist_t)]))
list(map(lambda i: (s_list.__setitem__(dist_s[i], s_list[dist_s[i]] + 1), 
                    t_list.__setitem__(dist_t[i], t_list[dist_t[i]] + 1)), range(n)))

mind = dist_s[t]
ans = reduce(add, map(lambda i: s_list[i] * t_list[mind - 2 - i], range(mind - 1)), 0)
print(ans)