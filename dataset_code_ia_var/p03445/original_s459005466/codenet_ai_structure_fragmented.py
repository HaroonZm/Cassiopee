from collections import deque, Counter
import sys

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 7)

def get_input():
    return sys.stdin.readline

def get_mod():
    return 10**9 + 7

def read_hw(input_func):
    h, w = map(int, input_func().split())
    return h, w

def read_n(input_func):
    n = int(input_func())
    return n

def init_answer():
    return 0

def init_black_row_column():
    black = []
    row = Counter()
    column = Counter()
    return black, row, column

def process_black(n, input_func, row, column, black):
    for _ in range(n):
        x, y = map(int, input_func().split())
        row[x] += 1
        column[y] += 1
        black.append((x, y))
    return row, column, black

def add_sentinels(row, column, h, w):
    row[h] += 1
    column[w] += 1
    return row, column

def sqsum(x):
    return x*(x+1)*(2*x+1)//6

def area_row_keys(row):
    return sorted(row.keys())

def process_row_keys(keys, row, w, h, n, mod):
    pre = -1
    top = 0
    bottom = h*w - n
    area = []
    ans = 0
    for i in keys:
        if i == pre+2:
            top, bottom = increment_top_bottom_by_w(top, bottom, w)
            area.append([-1, 1])
        elif i > pre+2:
            ans = add_area_answer(ans, i, pre, top, bottom, w, mod)
            top, bottom = increment_top_bottom_large_gap(top, bottom, i, pre, w)
            area.append([-1, i-pre-1])
        if i != h:
            top, bottom = inc_top_bottom_exclude_row(top, bottom, w, row[i])
            area.append([i])
        pre = i
    return area, ans

def increment_top_bottom_by_w(top, bottom, w):
    top += w
    bottom -= w
    return top, bottom

def add_area_answer(ans, i, pre, top, bottom, w, mod):
    val = (i-pre-2)*top*bottom + ((i-pre-2)*(i-pre-1)//2) * w*(bottom-top) - sqsum(i-pre-2)*(w**2)
    ans += val
    ans %= mod
    return ans

def increment_top_bottom_large_gap(top, bottom, i, pre, w):
    top += (i-pre-1)*w
    bottom -= (i-pre-1)*w
    return top, bottom

def inc_top_bottom_exclude_row(top, bottom, w, rowi):
    top += w-rowi
    bottom -= w-rowi
    return top, bottom

def get_R(area):
    return len(area)

def area_column_keys(column):
    return sorted(column.keys())

def process_column_keys(keys, column, area, black, h, w, n, mod):
    pre = -1
    left = 0
    right = h*w - n
    R = len(area)
    area2 = []
    ans = 0
    for j in keys:
        if j == pre+2:
            left, right = increment_left_right_by_h(left, right, h)
            area2.append([area[i][1] if area[i][0] == -1 else 1 for i in range(R)])
        elif j > pre+2:
            ans = add_col_area_answer(ans, j, pre, left, right, h, mod)
            left, right = increment_left_right_large_gap(left, right, j, pre, h)
            area2.append([(j-pre-1)*area[i][1] if area[i][0]==-1 else (j-pre-1) for i in range(R)])
        if j != w:
            left, right = inc_left_right_exclude_column(left, right, h, column[j])
            tmp = []
            for i in range(R):
                if area[i][0] == -1:
                    tmp.append(area[i][1])
                else:
                    if (area[i][0], j) in black:
                        tmp.append(0)
                    else:
                        tmp.append(1)
            area2.append(tmp)
        pre = j
    return area2, ans

def increment_left_right_by_h(left, right, h):
    left += h
    right -= h
    return left, right

def add_col_area_answer(ans, j, pre, left, right, h, mod):
    val = (j-pre-2)*left*right + ((j-pre-2)*(j-pre-1)//2) * h*(right-left) - sqsum(j-pre-2)*(h**2)
    ans += val
    ans %= mod
    return ans

def increment_left_right_large_gap(left, right, j, pre, h):
    left += (j-pre-1)*h
    right -= (j-pre-1)*h
    return left, right

def inc_left_right_exclude_column(left, right, h, columnj):
    left += h-columnj
    right -= h-columnj
    return left, right

def get_C(area2):
    return len(area2)

def transpose_area2(area2, R, C):
    return [[area2[j][i] for j in range(C)] for i in range(R)]

def get_vec():
    return [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(p, q, area2, R, C, vec):
    dist = [[10**5 for _ in range(C)] for __ in range(R)]
    visited = [[False for _ in range(C)] for __ in range(R)]
    dist[p][q] = 0
    visited[p][q] = True
    qu = deque([(p, q)])
    while qu:
        x, y = qu.popleft()
        for dx, dy in vec:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < R and 0 <= ny < C and area2[nx][ny] != 0:
                if not visited[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                    qu.append((nx, ny))
    return dist

def calc_ans2(area2, R, C, vec, mod):
    ans2 = 0
    for x in range(R*C):
        i = x // C
        j = x % C
        if area2[i][j] == 0:
            continue
        d = bfs(i, j, area2, R, C, vec)
        for y in range(R*C):
            k = y // C
            l = y % C
            if area2[k][l] == 0:
                continue
            ans2 += area2[i][j]*area2[k][l]*d[k][l]
            ans2 %= mod
    ans2 = finalize_ans2(ans2, mod)
    return ans2

def finalize_ans2(ans2, mod):
    ans2 *= pow(2, mod-2, mod)
    return ans2

def print_final_answer(ans, ans2, mod):
    print((ans+ans2) % mod)

def main():
    set_recursion_limit()
    input_func = get_input()
    mod = get_mod()
    h, w = read_hw(input_func)
    n = read_n(input_func)

    ans = init_answer()
    black, row, column = init_black_row_column()
    row, column, black = process_black(n, input_func, row, column, black)
    row, column = add_sentinels(row, column, h, w)

    area, ans_row = process_row_keys(area_row_keys(row), row, w, h, n, mod)
    ans = (ans + ans_row) % mod
    R = get_R(area)

    area2, ans_col = process_column_keys(area_column_keys(column), column, area, black, h, w, n, mod)
    ans = (ans + ans_col) % mod
    C = get_C(area2)

    area2 = transpose_area2(area2, R, C)
    vec = get_vec()
    ans2 = calc_ans2(area2, R, C, vec, mod)
    print_final_answer(ans, ans2, mod)

main()