def main():
    while True:
        n = get_input_size()
        if is_end_input(n):
            break
        to = create_empty_to()
        fr = create_empty_fr(n)
        read_and_fill_mappings(n, to, fr)
        order = create_empty_order()
        used = create_unused_list(n)
        compute_order(n, to, used, order)
        used = create_unused_list(n)
        ans = process_scc(order, fr, used, n)
        print_result(ans)

def get_input_size():
    return int(input())

def is_end_input(n):
    return n == 0

def create_empty_to():
    return []

def create_empty_fr(n):
    return [[] for _ in range(n * n)]

def read_and_fill_mappings(n, to, fr):
    for i in range(n):
        line = read_line_of_integers()
        process_line(i, n, line, to, fr)

def read_line_of_integers():
    return list(map(int, input().split()))

def process_line(i, n, line, to, fr):
    for j in range(n):
        x, y = extract_xy(line, j)
        idx_to = get_index(y, n, x)
        idx_fr = get_index(i, n, j)
        to.append(idx_to)
        fr[idx_to].append(idx_fr)

def extract_xy(line, j):
    return line[2 * j], line[2 * j + 1]

def get_index(row, n, col):
    return row * n + col

def create_empty_order():
    return []

def create_unused_list(n):
    return [False] * (n * n)

def compute_order(n, to, used, order):
    for i in range(n * n):
        dfs(i, to, used, order)

def dfs(x, to, used, order):
    if already_used(used, x):
        return
    mark_used(used, x)
    next_node = get_next_node(to, x)
    dfs(next_node, to, used, order)
    add_to_order(order, x)

def already_used(used, x):
    return used[x]

def mark_used(used, x):
    used[x] = True

def get_next_node(to, x):
    return to[x]

def add_to_order(order, x):
    order.append(x)

def process_scc(order, fr, used, n):
    ans = 0
    for i in order:
        group = create_empty_group()
        if not already_used(used, i):
            dfs2(i, used, group, fr)
        if is_valid_group(group):
            ans = increment_ans(ans)
    return ans

def create_empty_group():
    return []

def dfs2(x, used, group, fr):
    if already_used(used, x):
        return
    mark_used(used, x)
    for f in get_fr_nodes(fr, x):
        dfs2(f, used, group, fr)
    add_to_group(group, x)

def get_fr_nodes(fr, x):
    return fr[x]

def add_to_group(group, x):
    group.append(x)

def is_valid_group(group):
    return len(group) >= 1

def increment_ans(ans):
    return ans + 1

def print_result(ans):
    print(ans)

main()