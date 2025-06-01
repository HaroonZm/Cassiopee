from heapq import heappop as pop
from heapq import heappush as push
INF = 1000000000000

def can_move_up(y, used):
    return y > 0 and not used[y - 1]

def can_move_down(y, h, used):
    return h > y + 1 and not used[y + 1]

def can_move_left(x, used):
    return x > 0 and not used[x - 1]

def can_move_right(x, w, used):
    return w > x + 1 and not used[x + 1]

def move_up(lst, used, que, y, x):
    push(que, (lst[y - 1][x], y - 1, x))
    used[y - 1][x] = True

def move_down(lst, used, que, y, x):
    push(que, (lst[y + 1][x], y + 1, x))
    used[y + 1][x] = True

def move_left(lst, used, que, y, x):
    push(que, (lst[y][x - 1], y, x - 1))
    used[y][x - 1] = True

def move_right(lst, used, que, y, x):
    push(que, (lst[y][x + 1], y, x + 1))
    used[y][x + 1] = True

def check_and_move_up(lst, used, que, y, x):
    if can_move_up(y, used):
        move_up(lst, used, que, y, x)

def check_and_move_down(lst, used, que, y, x, h):
    if can_move_down(y, h, used):
        move_down(lst, used, que, y, x)

def check_and_move_left(lst, used, que, y, x):
    if can_move_left(x, used[y]):
        move_left(lst, used, que, y, x)

def check_and_move_right(lst, used, que, y, x, w):
    if can_move_right(x, w, used[y]):
        move_right(lst, used, que, y, x)

def process_neighbors(lst, used, que, w, h, y, x):
    check_and_move_up(lst, used, que, y, x)
    check_and_move_down(lst, used, que, y, x, h)
    check_and_move_left(lst, used, que, y, x)
    check_and_move_right(lst, used, que, y, x, w)

def bfs(lst, used, que, w, h):
    v, y, x = pop(que)
    process_neighbors(lst, used, que, w, h, y, x)
    return v

def increment_accumulator(acc):
    return acc + 1

def update_max_and_dic(Max, v, dic, acc):
    if v > Max:
        dic.append([v, acc])
        Max = v
    else:
        dic[-1][1] += 1
    return Max

def initialize_used(w, h):
    return [[False] * w for _ in range(h)]

def initialize_que(x, y):
    return [(1, y, x)]

def make_dic(lst, w, h, x, y):
    que = initialize_que(x, y)
    used = initialize_used(w, h)
    used[y][x] = True
    dic = [[0, 0]]
    Max = 0
    acc = 0
    while que:
        v = bfs(lst, used, que, w, h)
        acc = increment_accumulator(acc)
        Max = update_max_and_dic(Max, v, dic, acc)
    return dic

def read_dimensions():
    w, h, x, y = map(int, input().split())
    return w, h, x - 1, y - 1

def read_lst(h, w):
    lst = []
    for _ in range(h):
        row = list(map(int, input().split()))
        lst.append(row)
    return lst

def find_min_sum(dic1, dic2, R):
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
            if rs < ans:
                ans = rs
            break
        else:
            if ind2 < end2 - 1:
                ind2 += 1
            r2 = dic2[ind2][0]
            rs = r1 + r2
            if rs < ans:
                ans = rs
        ind1 += 1
    return ans

def process_case(R):
    w1, h1, x1, y1 = read_dimensions()
    lst1 = read_lst(h1, w1)
    w2, h2, x2, y2 = read_dimensions()
    lst2 = read_lst(h2, w2)
    dic1 = make_dic(lst1, w1, h1, x1, y1)
    dic2 = make_dic(lst2, w2, h2, x2, y2)
    ans = find_min_sum(dic1, dic2, R)
    print(ans)

def solve():
    while True:
        R = int(input())
        if not R:
            break
        process_case(R)

solve()