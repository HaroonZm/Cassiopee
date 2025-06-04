from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    return list(map(list, sys.stdin.readline().split()))

def S():
    return list(sys.stdin.readline())[:-1]

def IR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

sys.setrecursionlimit(1000000)
mod = 1000000007

def process_l_input(n):
    l = LIR(n)
    return l

def sort_by_second_element(l):
    l.sort(key=lambda x: x[1])
    return l

def extract_and_sort_first_column(l, n):
    r = [l[i][0] for i in range(n)]
    r.sort()
    return r

def initialize_counter_arrays():
    s = [0 for _ in range(100001)]
    f = [0 for _ in range(100001)]
    return s, f

def fill_counter_arrays_and_frequencies(l, s, f):
    for a, b in l:
        s[a] += 1
        s[b] -= 1
        f[b] += 1

def accumulate_s_f(s, f):
    for i in range(100000):
        s[i+1] += s[i]
        f[i+1] += f[i]

def get_ri(r, b, n):
    ri = bisect.bisect_left(r, b)
    ri = n - ri
    return ri

def get_le(f, a):
    return f[a]

def update_ans(ans, val):
    return max(ans, val)

def get_max_s(s):
    return max(s)

def D():
    n = I()
    s, f = initialize_counter_arrays()
    l = process_l_input(n)
    l = sort_by_second_element(l)
    r = extract_and_sort_first_column(l, n)
    fill_counter_arrays_and_frequencies(l, s, f)
    accumulate_s_f(s, f)
    ans = 0
    for a, b in l:
        ri = get_ri(r, b, n)
        le = get_le(f, a)
        ans = update_ans(ans, n - (ri + le))
    print(ans, get_max_s(s))
    return

def process_vars_for_A():
    n, k = LI()
    return n, k

def compute_s_for_A(j, i):
    s = 1
    for a in range(i):
        s *= j - a
        s //= a + 1
    return s

def process_loops_for_A(n, k):
    ans = 0
    for l in range(1, n+1):
        for i in range(1000):
            if i * k > l:
                break
            j = l - i * k + i
            if j % 2:
                j //= 2
                j += 1
                s = compute_s_for_A(j, i)
                ans += s
    return ans

def A():
    n, k = process_vars_for_A()
    ans = process_loops_for_A(n, k)
    print(ans)
    return

def B():
    return

def process_input_list_C(n):
    v = [input().split() for _ in range(n)]
    return v

def build_d_and_update_v(v, n):
    d = defaultdict(int)
    s = 0
    i = 0
    while i < n:
        v[i][1] = int(v[i][1])
        v[i][2] = int(v[i][2])
        if v[i][2] == 0:
            s += v[i][1]
            v.pop(i)
            n -= 1
        else:
            d[v[i][0]] = i
            i += 1
    return v, d, n, s

def build_f_matrix(n):
    return [[1 for _ in range(n)] for _ in range(n)]

def update_f_matrix_from_v(v, n, d, f):
    for i in range(n):
        for j in v[i][3:]:
            f[i][d[j]] = 0

def build_e_matrix(n, f):
    e = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if f[i][j]:
                e[i].append(j)
    return e

def proceed_C():
    while 1:
        n = I()
        if n == 0:
            break
        v = process_input_list_C(n)
        v, d, n, s = build_d_and_update_v(v, n)
        f = build_f_matrix(n)
        update_f_matrix_from_v(v, n, d, f)
        e = build_e_matrix(n, f)
        for i in e:
            print(i)
        print(s)
    return

def C():
    proceed_C()
    return

def process_c_for_E(n):
    c = LI()
    return c

def build_f_sorted_for_E(c, n):
    f = [[i, c[i]] for i in range(n)]
    f.sort(key=lambda x: x[1])
    return f

def process_v_for_E(n, m):
    v = [[] for _ in range(n)]
    for _ in range(m):
        a, b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    return v

def initialize_bfs_E(n):
    q = deque()
    bfs_map = [1 for _ in range(n)]
    ans = [0 for _ in range(n)]
    return q, bfs_map, ans

def bfs_process_for_E(f, v, bfs_map, ans, q):
    for i, _ in f:
        if not bfs_map[i]:
            continue
        q.append((i, -1))
        bfs_map[i] = 0
        ans[i] = 1
        while q:
            x, pre = q.popleft()
            for y in v[x]:
                if bfs_map[y]:
                    if x == 0:
                        bfs_map[y] = 0
                        q.append((y, x))

def E():
    n = I()
    c = process_c_for_E(n)
    f = build_f_sorted_for_E(c, n)
    m = I()
    v = process_v_for_E(n, m)
    q, bfs_map, ans = initialize_bfs_E(n)
    bfs_process_for_E(f, v, bfs_map, ans, q)
    print(sum(ans))
    return

def F():
    return

def G():
    return

def H():
    return

def I_():
    return

def J():
    return

if __name__ == "__main__":
    D()