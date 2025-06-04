import sys
from collections import deque

def read_input():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    EDGE = [list(map(int, input().split())) for _ in range(N-1)]
    Query = [list(map(int, input().split())) for _ in range(Q)]
    return N, Q, EDGE, Query

def make_empty_edgelist(N):
    return [dict() for _ in range(N+1)]

def build_edgelist(EDGE, EDGELIST):
    for x, y, c, l in EDGE:
        EDGELIST[x][y] = (c, l)
        EDGELIST[y][x] = (c, l)

def init_depth_and_used(N):
    DEPTH = [-1]*(N+1)
    DEPTH[1] = 0
    USED = [0]*(N+1)
    return DEPTH, USED

def make_euler_tour(N, EDGELIST, DEPTH, USED):
    QUE = deque([1])
    QUE2 = deque()
    EULER = []
    while QUE:
        process_euler_tour(QUE, QUE2, EULER, DEPTH, EDGELIST, USED)
    return EULER

def process_euler_tour(QUE, QUE2, EULER, DEPTH, EDGELIST, USED):
    x = QUE.pop()
    EULER.append((DEPTH[x], x))
    if USED[x] == 1:
        return
    for to in EDGELIST[x]:
        handle_possible_move(x, to, DEPTH, USED, QUE2)
    extend_queue(QUE, QUE2)
    USED[x] = 1

def handle_possible_move(x, to, DEPTH, USED, QUE2):
    if USED[to] == 0:
        DEPTH[to] = DEPTH[x]+1
        QUE2.append(to)

def extend_queue(QUE, QUE2):
    QUE.extend(QUE2)
    QUE2.clear()

def min_max_p_from_euler(N, EULER):
    MINP = [(1<<30)]*(N+1)
    MAXP = [(-1)]*(N+1)
    for ind, (depth, p) in enumerate(EULER):
        MINP[p] = min(MINP[p], ind)
        MAXP[p] = max(MAXP[p], ind)
    return MINP, MAXP

def make_segment_elements(LEN):
    return 1<<(LEN.bit_length())

def init_segment(seg_el):
    return [(1<<30, 0)]*(2*seg_el)

def update_segment_base(SEG, seg_el, EULER):
    for i in range(len(EULER)):
        SEG[i+seg_el] = EULER[i]

def build_segment_tree(SEG, seg_el):
    for i in range(seg_el-1, 0, -1):
        SEG[i] = min(SEG[i*2], SEG[i*2+1])

def update(n, x, seg_el, SEG):
    i = n + seg_el
    SEG[i] = x
    i >>= 1
    while i != 0:
        SEG[i] = min(SEG[i*2], SEG[i*2+1])
        i >>= 1

def getvalues(l, r, seg_el, SEG):
    L = l + seg_el
    R = r + seg_el
    ANS = (1<<30, 0)
    while L < R:
        if L & 1:
            ANS = min(ANS, SEG[L])
            L += 1
        if R & 1:
            R -= 1
            ANS = min(ANS, SEG[R])
        L >>= 1
        R >>= 1
    return ANS

def LCA(l, r, MINP, MAXP, seg_el, SEG):
    return getvalues(min(MINP[l], MINP[r]), max(MAXP[l], MAXP[r])+1, seg_el, SEG)

def prepare_lca_queries(N, Query, LCA_func):
    check = [set() for _ in range(N+1)]
    for c, l, x, y in Query:
        check[x].add(c)
        check[y].add(c)
        lca = LCA_func(x, y)[1]
        check[lca].add(c)
    return check

def init_length_arrays(N):
    LENGTH = [0]*(N+1)
    LENG = 0
    C_LENGTH = [0]*N
    C_SUM = [0]*N
    C_LDICT = dict()
    C_SDICT = dict()
    return LENGTH, LENG, C_LENGTH, C_SUM, C_LDICT, C_SDICT

def reset_ind_dicts(check, C_LDICT, C_SDICT):
    for c in check[1]:
        C_LDICT[(1, c)] = 0
        C_SDICT[(1, c)] = 0

def process_euler_indices(EULER, EDGELIST, check, LENGTH, LENG, C_LENGTH, C_SUM, C_LDICT, C_SDICT):
    for i in range(1, len(EULER)):
        update_euler_index(i, EULER, EDGELIST, check, LENGTH, C_LENGTH, C_SUM, C_LDICT, C_SDICT)

def update_euler_index(i, EULER, EDGELIST, check, LENGTH, C_LENGTH, C_SUM, C_LDICT, C_SDICT):
    ind = EULER[i][1]
    c, l = EDGELIST[EULER[i-1][1]][ind]
    if EULER[i][0] > EULER[i-1][0]:
        update_euler_up(ind, l, c, LENGTH, C_LENGTH, C_SUM, check, C_LDICT, C_SDICT)
    else:
        update_euler_down(l, c, C_LENGTH, C_SUM)

def update_euler_up(ind, l, c, LENGTH, C_LENGTH, C_SUM, check, C_LDICT, C_SDICT):
    LENGTH[ind] += l if LENGTH[ind] == 0 else 0
    C_LENGTH[c] += l
    C_SUM[c] += 1
    LENGTH[ind] = sum_length_up(LENGTH, ind, l)
    for q_c in check[ind]:
        C_LDICT[(ind, q_c)] = C_LENGTH[q_c]
        C_SDICT[(ind, q_c)] = C_SUM[q_c]

def sum_length_up(LENGTH, ind, l):
    if LENGTH[ind] == 0:
        return l + LENGTH[ind]
    return LENGTH[ind]

def update_euler_down(l, c, C_LENGTH, C_SUM):
    C_LENGTH[c] -= l
    C_SUM[c] -= 1

def process_queries(Query, LCA_func, LENGTH, C_SDICT, C_LDICT):
    for c, pl, x, y in Query:
        process_single_query(c, pl, x, y, LCA_func, LENGTH, C_SDICT, C_LDICT)

def process_single_query(c, pl, x, y, LCA_func, LENGTH, C_SDICT, C_LDICT):
    ind = LCA_func(x, y)[1]
    ans = (LENGTH[x] + LENGTH[y] - LENGTH[ind]*2
           + (C_SDICT.get((x, c), 0) + C_SDICT.get((y, c), 0) - C_SDICT.get((ind, c), 0)*2) * pl
           - (C_LDICT.get((x, c), 0) + C_LDICT.get((y, c), 0) - C_LDICT.get((ind, c), 0)*2))
    print(ans)

def main():
    N, Q, EDGE, Query = read_input()
    mod = 10**9+7
    EDGELIST = make_empty_edgelist(N)
    build_edgelist(EDGE, EDGELIST)
    DEPTH, USED = init_depth_and_used(N)
    EULER = make_euler_tour(N, EDGELIST, DEPTH, USED)
    MINP, MAXP = min_max_p_from_euler(N, EULER)
    LEN = len(EULER)
    seg_el = make_segment_elements(LEN)
    SEG = init_segment(seg_el)
    update_segment_base(SEG, seg_el, EULER)
    build_segment_tree(SEG, seg_el)

    def LCA_func(l, r):
        return LCA(l, r, MINP, MAXP, seg_el, SEG)

    check = prepare_lca_queries(N, Query, LCA_func)
    LENGTH, LENG, C_LENGTH, C_SUM, C_LDICT, C_SDICT = init_length_arrays(N)
    reset_ind_dicts(check, C_LDICT, C_SDICT)
    process_euler_indices(EULER, EDGELIST, check, LENGTH, LENG, C_LENGTH, C_SUM, C_LDICT, C_SDICT)
    process_queries(Query, LCA_func, LENGTH, C_SDICT, C_LDICT)

main()