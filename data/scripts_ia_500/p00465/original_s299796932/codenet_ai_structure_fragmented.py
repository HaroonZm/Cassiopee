from heapq import heappop as pop
from heapq import heappush as push
INF = 1000000000000

def is_used(used, y, x):
    return used[y][x]

def mark_used(used, y, x):
    used[y][x] = True

def get_value(lst, y, x):
    return lst[y][x]

def push_node(que, value, y, x):
    push(que, (value, y, x))

def bfs_pop(que):
    return pop(que)

def check_and_push_up(lst, used, que, y, x):
    ny = y - 1
    nx = x
    if not is_used(used, ny, nx):
        val = get_value(lst, ny - 1, nx - 1)
        push_node(que, val, ny, nx)
        mark_used(used, ny, nx)

def check_and_push_down(lst, used, que, y, x):
    ny = y + 1
    nx = x
    if not is_used(used, ny, nx):
        val = get_value(lst, ny - 1, nx - 1)
        push_node(que, val, ny, nx)
        mark_used(used, ny, nx)

def check_and_push_left(lst, used, que, y, x):
    ny = y
    nx = x - 1
    if not is_used(used, ny, nx):
        val = get_value(lst, ny - 1, nx - 1)
        push_node(que, val, ny, nx)
        mark_used(used, ny, nx)

def check_and_push_right(lst, used, que, y, x):
    ny = y
    nx = x + 1
    if not is_used(used, ny, nx):
        val = get_value(lst, ny - 1, nx - 1)
        push_node(que, val, ny, nx)
        mark_used(used, ny, nx)

def bfs(lst, used, que, w, h):
    v, y, x = bfs_pop(que)
    check_and_push_up(lst, used, que, y, x)
    check_and_push_down(lst, used, que, y, x)
    check_and_push_left(lst, used, que, y, x)
    check_and_push_right(lst, used, que, y, x)
    return v

def create_used_grid(w, h):
    used = [[True] * (w + 2)]
    for _ in range(h):
        used.append([True] + [False] * w + [True])
    used.append([True] * (w + 2))
    return used

def initialize_used(used, y, x):
    mark_used(used, y, x)

def create_queue(y, x):
    return [(1, y, x)]

def create_dic():
    return [[0, 0]]

def append_to_dic(dic, item):
    dic.append(item)

def update_dic_last(dic):
    dic[-1][1] += 1

def make_dic(lst, w, h, x, y):
    que = create_queue(y, x)
    used = create_used_grid(w, h)
    initialize_used(used, y, x)
    dic = create_dic()
    Max = 0
    acc = 0
    while que:
        v = bfs(lst, used, que, w, h)
        acc += 1
        if v > Max:
            append_to_dic(dic, [v, acc])
            Max = v
        else:
            update_dic_last(dic)
    return dic

def input_int():
    return int(input())

def input_map():
    return map(int, input().split())

def input_list(h):
    return [list(map(int, input().split())) for _ in range(h)]

def load_single_case():
    w, h, x, y = input_map()
    lst = input_list(h)
    return w, h, x, y, lst

def get_len(dic):
    return len(dic)

def get_item(dic, index):
    return dic[index]

def update_index(ind, step=1):
    return ind + step

def update_index_reverse(ind, step=1):
    return ind - step

def is_less(val1, val2):
    return val1 < val2

def is_less_equal(val1, val2):
    return val1 <= val2

def main_loop_condition(ind1, end1, ind2):
    return ind1 < end1 and ind2 > 0

def sum_values(val1, val2):
    return val1 + val2

def solve():
    while True:
        R = input_int()
        if R == 0:
            break
        w1, h1, x1, y1, lst1 = load_single_case()
        w2, h2, x2, y2, lst2 = load_single_case()
        dic1 = make_dic(lst1, w1, h1, x1, y1)
        dic2 = make_dic(lst2, w2, h2, x2, y2)
        end1 = get_len(dic1)
        end2 = get_len(dic2)
        ind1 = 0
        ind2 = end2 - 1
        ans = INF
        while main_loop_condition(ind1, end1, ind2):
            r1, sum1 = get_item(dic1, ind1)
            r2, sum2 = get_item(dic2, ind2)
            if sum_values(sum1, sum2) < R:
                ind1 = update_index(ind1)
                continue
            while ind2 > 0 and sum_values(sum1, sum2) >= R:
                ind2 = update_index_reverse(ind2)
                r2, sum2 = get_item(dic2, ind2)
            if ind2 == 0 and sum_values(sum1, sum2) >= R:
                rs = r1 + r2
                if is_less(rs, ans):
                    ans = rs
                break
            else:
                ind2 = update_index(ind2)
                r2 = dic2[ind2][0]
                rs = r1 + r2
                if is_less(rs, ans):
                    ans = rs
            ind1 = update_index(ind1)
        print(ans)

solve()