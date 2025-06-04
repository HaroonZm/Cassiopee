def read_input():
    return list(map(int, input().split()))

def initialize_parent(n, m):
    return list(range(n + m))

def find_root(x, parent):
    if x == parent[x]:
        return x
    parent[x] = find_root(parent[x], parent)
    return parent[x]

def unite_sets(x, y, parent):
    px = find_root(x, parent)
    py = find_root(y, parent)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def process_type1(b, c, m, parent, idx):
    pb = find_root(m + b, parent)
    pc = find_root(m + c, parent)
    if both_roots_in_first_m(pb, pc, m) and pb != pc:
        report_and_exit(idx)
    unite_sets(pb, pc, parent)
    return False

def both_roots_in_first_m(pb, pc, m):
    return pb < m and pc < m

def process_type2(b, c, m, parent, idx):
    pb = find_root(m + b, parent)
    if pb < m and pb != c:
        report_and_exit(idx)
    unite_sets(c, pb, parent)
    return False

def report_and_exit(idx):
    print(idx + 1)
    exit()

def handle_operation(operation, m, parent, idx):
    a, b, c = operation
    b -= 1
    c -= 1
    if a == 1:
        process_type1(b, c, m, parent, idx)
    else:
        process_type2(b, c, m, parent, idx)

def process_operations(k, m, parent):
    for idx in range(k):
        operation = read_input()
        handle_operation(operation, m, parent, idx)
    print(0)

def main():
    n, m, k = read_input()
    parent = initialize_parent(n, m)
    process_operations(k, m, parent)

main()