from heapq import heappop as pop
from heapq import heappush as push
INF = 1000000000000

def pop_from_queue(que):
    return pop(que)

def check_and_push_up(lst, used, que, y, x):
    if not used[y - 1][x]:
        push(que, (lst[y - 2][x - 1], y - 1, x))
        used[y - 1][x] = True

def check_and_push_down(lst, used, que, y, x):
    if not used[y + 1][x]:
        push(que, (lst[y][x - 1], y + 1, x))
        used[y + 1][x] = True

def check_and_push_left(lst, used, que, y, x):
    if not used[y][x - 1]:
        push(que, (lst[y - 1][x - 2], y, x - 1))
        used[y][x - 1] = True

def check_and_push_right(lst, used, que, y, x):
    if not used[y][x + 1]:
        push(que, (lst[y - 1][x], y, x + 1))
        used[y][x + 1] = True

def bfs(lst, used, que, w, h):
    v, y, x = pop_from_queue(que)
    check_and_push_up(lst, used, que, y, x)
    check_and_push_down(lst, used, que, y, x)
    check_and_push_left(lst, used, que, y, x)
    check_and_push_right(lst, used, que, y, x)
    return v

def create_used_matrix(w, h):
    used = [[True] + [False] * w + [True] for _ in range(h)]
    used.insert(0, [True] * (w + 2))
    used.append([True] * (w + 2))
    return used

def initialize_used(used, y, x):
    used[y][x] = True

def initialize_queue(y, x):
    return [(1, y, x)]

def initialize_dic():
    dic = [[0, 0]]
    return dic

def append_to_dic(dic, value):
    dic.append(value)

def update_max(dic, Max, v, acc):
    append_to_dic(dic, [v, acc])
    Max = v
    return Max

def increment_last_dic_count(dic):
    dic[-1][1] += 1

def make_dic(lst, w, h, x, y):
    que = initialize_queue(y, x)
    used = create_used_matrix(w, h)
    initialize_used(used, y, x)
    dic = initialize_dic()
    Max = 0
    acc = 0
    while que:
        v = bfs(lst, used, que, w, h)
        acc += 1
        if v > Max:
            Max = update_max(dic, Max, v, acc)
        else:
            increment_last_dic_count(dic)
    return dic

def input_int():
    return int(input())

def input_ints():
    return map(int, input().split())

def input_matrix(h):
    return [list(map(int, input().split())) for _ in range(h)]

def read_first_input():
    return input_int()

def read_rectangle_params():
    return list(input_ints())

def read_rectangle_matrix(h):
    return input_matrix(h)

def define_indices(dic):
    end = len(dic)
    ind_start = 0
    ind_end = end - 1
    return ind_start, ind_end, end

def update_best_answer(ans, candidate):
    if candidate < ans:
        ans = candidate
    return ans

def print_answer(ans):
    print(ans)

def loop_ind1_ind2(R, dic1, dic2):
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
            ind2 -= 1
            r2, sum2 = dic2[ind2]
        if ind2 == 0 and sum1 + sum2 >= R:
            rs = r1 + r2
            ans = update_best_answer(ans, rs)
            break
        else:
            ind2 += 1
            r2 = dic2[ind2][0]
            rs = r1 + r2
            ans = update_best_answer(ans, rs)
        ind1 += 1
    return ans

def solve():
    while True:
        R = read_first_input()
        if not R:
            break
        w1, h1, x1, y1 = read_rectangle_params()
        lst1 = read_rectangle_matrix(h1)
        w2, h2, x2, y2 = read_rectangle_params()
        lst2 = read_rectangle_matrix(h2)
        dic1 = make_dic(lst1, w1, h1, x1, y1)
        dic2 = make_dic(lst2, w2, h2, x2, y2)
        ans = loop_ind1_ind2(R, dic1, dic2)
        print_answer(ans)

solve()