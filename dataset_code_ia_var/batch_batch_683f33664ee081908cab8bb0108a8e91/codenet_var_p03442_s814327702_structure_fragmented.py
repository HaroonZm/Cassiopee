def read_input():
    return int(input())

def initialize_nodes(n):
    return [0] * n

def read_edges(n, nodes):
    for _ in range(n - 1):
        process_edge(nodes)

def process_edge(nodes):
    x, y, a = map(int, input().split())
    update_nodes(nodes, x, y, a)

def update_nodes(nodes, x, y, a):
    nodes[x] ^= a
    nodes[y] ^= a

def count_values(nodes):
    return Counter(nodes)

def remove_zero_from_counter(c):
    if 0 in c:
        del c[0]

def calculate_ans_and_remains(c):
    ans = 0
    remains = set()
    for i, v in c.items():
        ans = update_ans(ans, v)
        update_remains(remains, v, i)
    return ans, remains

def update_ans(ans, v):
    return ans + (v // 2)

def update_remains(remains, v, i):
    if v % 2:
        remains.add(i)

def perform_combinations(remains, ans):
    for r in (3, 4, 5):
        ans, remains = process_r_combinations(remains, ans, r)
    return ans

def process_r_combinations(remains, ans, r):
    while not r < len(remains) < r * 2:
        found = False
        for ns in generate_combinations(remains, r):
            if check_xor_zero(ns):
                remains = update_remains_set(remains, ns)
                ans = increment_ans(ans, r)
                found = True
                break
        if not found:
            break
    return ans, remains

def generate_combinations(remains, r):
    return combinations(remains, r)

def check_xor_zero(ns):
    return reduce(xor, ns) == 0

def update_remains_set(remains, ns):
    remains = set(remains)
    remains.difference_update(ns)
    return remains

def increment_ans(ans, r):
    return ans + (r - 1)

def print_result(ans):
    print(ans)

def main():
    n = read_input()
    nodes = initialize_nodes(n)
    read_edges(n, nodes)
    c = count_values(nodes)
    remove_zero_from_counter(c)
    ans, remains = calculate_ans_and_remains(c)
    ans = perform_combinations(remains, ans)
    print_result(ans)

main()