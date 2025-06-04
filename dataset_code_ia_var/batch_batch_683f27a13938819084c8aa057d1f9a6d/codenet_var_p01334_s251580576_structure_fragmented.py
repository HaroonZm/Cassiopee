def read_n():
    return int(input())

def read_lines(n):
    lines = []
    for _ in range(n):
        lines.append(list(map(int, input().split())))
    return lines

def flatten_indices(line, n, j):
    x, y = line[2*j:2*j+2]
    return y * n + x

def build_to(lines, n):
    to = []
    for i in range(n):
        line = lines[i]
        for j in range(n):
            to.append(flatten_indices(line, n, j))
    return to

def init_used(size):
    return [False] * size

def dfs_all(n, to):
    order = []
    used = init_used(n * n)
    for i in range(n * n):
        dfs(i, to, used, order)
    order.reverse()
    return order

def dfs(x, to, used, order):
    if used[x]:
        return
    used[x] = True
    dfs(to[x], to, used, order)
    order.append(x)

def dfs2(x, to, used, group):
    if used[x]:
        return False
    if x in group:
        return True
    group.add(x)
    return dfs2(to[x], to, used, group)

def process_order(n, to, order):
    used = init_used(n * n)
    ans = 0
    for i in order:
        group = set()
        if not used[i]:
            if dfs2(i, to, used, group):
                ans += 1
        update_used_from_group(group, used)
    return ans

def update_used_from_group(group, used):
    for g in group:
        used[g] = True

def main_loop():
    while True:
        n = read_n()
        if n == 0:
            break
        lines = read_lines(n)
        to = build_to(lines, n)
        order = dfs_all(n, to)
        ans = process_order(n, to, order)
        print(ans)

main_loop()