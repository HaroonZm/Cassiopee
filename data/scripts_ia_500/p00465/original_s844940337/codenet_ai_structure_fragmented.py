from heapq import heappop as pop
from heapq import heappush as push
INF = 1000000000000

def can_go_up(y):
    return y > 0

def can_go_down(y, h):
    return y + 1 < h

def can_go_left(x):
    return x > 0

def can_go_right(x, w):
    return x + 1 < w

def push_up(lst, used, que, y, x):
    push(que, (lst[y - 1][x], y - 1, x))
    used[y - 1][x] = True

def push_down(lst, used, que, y, x):
    push(que, (lst[y + 1][x], y + 1, x))
    used[y + 1][x] = True

def push_left(lst, used, que, y, x):
    push(que, (lst[y][x - 1], y, x - 1))
    used[y][x - 1] = True

def push_right(lst, used, que, y, x):
    push(que, (lst[y][x + 1], y, x + 1))
    used[y][x + 1] = True

def bfs(lst, used, que, w, h):
    v, y, x = pop(que)
    if can_go_up(y) and not used[y - 1][x]:
        push_up(lst, used, que, y, x)
    if can_go_down(y, h) and not used[y + 1][x]:
        push_down(lst, used, que, y, x)
    if can_go_left(x) and not used[y][x - 1]:
        push_left(lst, used, que, y, x)
    if can_go_right(x, w) and not used[y][x + 1]:
        push_right(lst, used, que, y, x)
    return v

def create_used_matrix(w, h):
    return [[False] * w for _ in range(h)]

def initialize_que_and_used(lst, w, h, x, y):
    que = [(1, y, x)]
    used = create_used_matrix(w, h)
    used[y][x] = True
    return que, used

def append_new(dic, v, acc):
    dic.append([v, acc])

def increment_count(dic):
    dic[-1][1] += 1

def update_max_and_dic(v, Max, acc, dic):
    if v > Max:
        append_new(dic, v, acc)
        Max = v
    else:
        increment_count(dic)
    return Max

def make_dic(lst, w, h, x, y):
    que, used = initialize_que_and_used(lst, w, h, x, y)
    dic = [[0, 0]]
    Max = 0
    acc = 0
    while que:
        v = bfs(lst, used, que, w, h)
        acc += 1
        Max = update_max_and_dic(v, Max, acc, dic)
    return dic

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_matrix(h, w):
    return [list(map(int, input().split())) for _ in range(h)]

def read_params():
    w, h, x, y = read_ints()
    return w, h, x, y

def read_all_inputs():
    R = read_int()
    if not R:
        return None
    w1, h1, x1, y1 = read_params()
    lst1 = read_matrix(h1, w1)
    w2, h2, x2, y2 = read_params()
    lst2 = read_matrix(h2, w2)
    return R, w1, h1, x1, y1, lst1, w2, h2, x2, y2, lst2

def update_answer(ans, rs):
    if rs < ans:
        ans = rs
    return ans

def move_ind2_down(dic2, ind2):
    ind2 -= 1
    r2, sum2 = dic2[ind2]
    return ind2, r2, sum2

def move_ind2_up(dic2, ind2):
    ind2 += 1
    r2 = dic2[ind2][0]
    return ind2, r2

def process_ind2_while(dic2, ind2, sum1, R):
    while ind2 > 0 and sum1 + dic2[ind2][1] >= R:
        ind2, r2, sum2 = move_ind2_down(dic2, ind2)
    return ind2

def main_loop(dic1, dic2, R):
    end1 = len(dic1)
    end2 = len(dic2)
    ind1 = 0
    ind2 = end2 - 1
    ans = INF
    while ind1 < end1 and ind2 > 0:
        r1, sum1 = dic1[ind1]
        r2, sum2 = dic2[ind2]
        if sum1 + sum2 < R:
            ind1 += 1
            continue
        while ind2 > 0 and sum1 + sum2 >= R:
            ind2, r2, sum2 = move_ind2_down(dic2, ind2)
        if ind2 == 0 and sum1 + sum2 >= R:
            rs = r1 + r2
            ans = update_answer(ans, rs)
            break
        else:
            ind2, r2 = move_ind2_up(dic2, ind2)
            rs = r1 + r2
            ans = update_answer(ans, rs)
        ind1 += 1
    return ans

def solve():
    while True:
        inputs = read_all_inputs()
        if inputs is None:
            break
        R, w1, h1, x1, y1, lst1, w2, h2, x2, y2, lst2 = inputs
        dic1 = make_dic(lst1, w1, h1, x1 - 1, y1 - 1)
        dic2 = make_dic(lst2, w2, h2, x2 - 1, y2 - 1)
        ans = main_loop(dic1, dic2, R)
        print(ans)

solve()