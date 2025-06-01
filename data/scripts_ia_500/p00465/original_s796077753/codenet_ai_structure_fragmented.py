from heapq import heappop as pop
from heapq import heappush as push
INF = 1000000000000

def can_go_up(y, used):
    return y > 0 and not used[y - 1]

def can_go_down(y, h, used):
    return y + 1 < h and not used[y + 1]

def can_go_left(x, used_row):
    return x > 0 and not used_row[x - 1]

def can_go_right(x, w, used_row):
    return x + 1 < w and not used_row[x + 1]

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
    v, y, x  = pop(que)
    if can_go_up(y, used):
        push_up(lst, used, que, y, x)
    if can_go_down(y, h, used):
        push_down(lst, used, que, y, x)
    if can_go_left(x, used[y]):
        push_left(lst, used, que, y, x)
    if can_go_right(x, w, used[y]):
        push_right(lst, used, que, y, x)
    return v

def create_used_matrix(h, w):
    return [[False] * w for _ in range(h)]

def initialize_queue(y, x):
    return [(1, y, x)]

def mark_used(used, y, x):
    used[y][x] = True

def initialize_dic():
    return [[0, 0]]

def get_append(dic):
    return dic.append

def update_max_and_append(dic, v, acc, Max):
    dic.append([v, acc])
    return v

def increment_last_count(dic):
    dic[-1][1] += 1

def make_dic(lst, w, h, x, y):
    que = initialize_queue(y, x)
    used = create_used_matrix(h, w)
    mark_used(used, y, x)
    dic = initialize_dic()
    app = get_append(dic)
    Max = 0
    acc = 0

    while que:
        v = bfs(lst, used, que, w, h)
        acc += 1
        if v > Max:
            Max = update_max_and_append(dic, v, acc, Max)
        else:
            increment_last_count(dic)
    return dic

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_grid(w, h):
    return [list(map(int, input().split())) for _ in range(h)]

def get_len(dic):
    return len(dic)

def get_r_sum(dic, idx):
    return dic[idx]

def increment(i):
    return i + 1

def decrement(i):
    return i - 1

def solve():
    while True:
        R = read_int()
        if R == 0:
            break
        w1, h1, x1, y1 = read_ints()
        lst1 = read_grid(w1, h1)

        w2, h2, x2, y2 = read_ints()
        lst2 = read_grid(w2, h2)

        dic1 = make_dic(lst1, w1, h1, x1 - 1, y1 - 1)
        dic2 = make_dic(lst2, w2, h2, x2 - 1, y2 - 1)

        end1 = get_len(dic1)
        end2 = get_len(dic2)
        ind1 = 0
        ind2 = end2 - 1
        ans = INF

        while ind1 < end1 and ind2 > 0:
            r1, sum1 = get_r_sum(dic1, ind1)
            r2, sum2 = get_r_sum(dic2, ind2)
            if sum1 + sum2 < R:
                ind1 = increment(ind1)
                continue
            while ind2 > 0 and sum1 + sum2 >= R:
                ind2 = decrement(ind2)
                r2, sum2 = get_r_sum(dic2, ind2)
            if ind2 == 0 and sum1 + sum2 >= R:
                rs = r1 + r2
                if rs < ans:
                    ans = rs
                break
            else:
                if ind2 < end2 - 1:
                    ind2 = increment(ind2)
                r2 = dic2[ind2][0]
                rs = r1 + r2
                if rs < ans:
                    ans = rs
            ind1 = increment(ind1)
        print(ans)

solve()