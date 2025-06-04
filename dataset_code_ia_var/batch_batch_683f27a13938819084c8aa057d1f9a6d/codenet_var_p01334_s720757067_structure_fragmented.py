def read_n():
    return int(input())

def read_lines(n):
    return [list(map(int, input().split())) for _ in range(n)]

def make_indices(n, line, i, j):
    x = line[2 * j]
    y = line[2 * j + 1]
    return x, y, y * n + x, i * n + j

def build_to_fr(n, lines):
    to = []
    fr = [[] for _ in range(n * n)]
    for i in range(n):
        line = lines[i]
        for j in range(n):
            x, y, idx_to, idx_fr = make_indices(n, line, i, j)
            to.append(idx_to)
            fr[idx_to].append(idx_fr)
    return to, fr

def dfs(x, used, to, order, call):
    if used[x]:
        return
    used[x] = True
    call(to[x], used, to, order, call)
    order.append(x)

def perform_dfs(n, to):
    order = []
    used = [False] * (n * n)
    for i in range(n * n):
        dfs(i, used, to, order, dfs)
    return order[::-1]

def dfs2_core(x, used, group, to, call):
    if used[x]:
        return False
    if x in group:
        return True
    group.append(x)
    ret = False
    ret = ret or call(to[x], used, group, to, call)
    return ret

def count_cycles(n, order, to):
    used = [False] * (n * n)
    ans = 0
    for i in order:
        group = []
        if not used[i]:
            if dfs2_core(i, used, group, to, dfs2_core):
                ans += 1
        for g in group:
            used[g] = True
    return ans

def process_one_case(n):
    lines = read_lines(n)
    to, fr = build_to_fr(n, lines)
    order = perform_dfs(n, to)
    ans = count_cycles(n, order, to)
    print(ans)

def main_loop():
    while True:
        n = read_n()
        if n == 0:
            break
        process_one_case(n)

main_loop()