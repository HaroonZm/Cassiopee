def read_n():
    return int(input())

def is_end(n):
    return n == 0

def read_line():
    return list(map(int, input().split()))

def process_input(n):
    to = []
    for i in range(n):
        line = read_line()
        to += process_line(line, n)
    return to

def process_line(line, n):
    coords = []
    for j in range(n):
        x, y = extract_coords(line, j)
        coords.append(y * n + x)
    return coords

def extract_coords(line, j):
    x = line[2 * j]
    y = line[2 * j + 1]
    return x, y

def reset_used(size):
    return [False] * size

def dfs_all(n, to):
    order = []
    used = reset_used(n * n)
    for i in range(n * n):
        dfs(i, to, used, order)
    reverse_list(order)
    return order

def dfs(x, to, used, order):
    if is_used(used, x):
        return
    set_used(used, x)
    dfs(to[x], to, used, order)
    order_append(order, x)

def is_used(used, x):
    return used[x]

def set_used(used, x):
    used[x] = True

def order_append(order, x):
    order.append(x)

def reverse_list(lst):
    lst.reverse()

def dfs2(x, to, used, group):
    if in_group(group, x):
        return True
    if is_used(used, x):
        return False
    add_to_group(group, x)
    set_used(used, x)
    return dfs2(to[x], to, used, group)

def in_group(group, x):
    return x in group

def add_to_group(group, x):
    group.add(x)

def count_groups(order, n, to):
    used = reset_used(n * n)
    ans = 0
    for i in order:
        group = new_group()
        if not is_used(used, i):
            if dfs2(i, to, used, group):
                ans = inc(ans)
    return ans

def new_group():
    return set()

def inc(x):
    return x + 1

def output(ans):
    print(ans)

def main_loop():
    while True:
        n = read_n()
        if is_end(n):
            break
        to = process_input(n)
        order = dfs_all(n, to)
        ans = count_groups(order, n, to)
        output(ans)

main_loop()