import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def generate_zero_list(n):
    return [0] * (n + 1)

def generate_parent_list(n):
    return [i for i in range(n + 1)]

def initialize_weighted_union_find(n):
    par = generate_parent_list(n)
    rank = generate_zero_list(n)
    weight = generate_zero_list(n)
    added = generate_zero_list(n)
    return {'par': par, 'rank': rank, 'weight': weight, 'added': added}

def get_parent(uf, x):
    return uf['par'][x]

def set_parent(uf, x, value):
    uf['par'][x] = value

def get_rank(uf, x):
    return uf['rank'][x]

def increment_rank(uf, x):
    uf['rank'][x] += 1

def get_weight(uf, x):
    return uf['weight'][x]

def set_weight(uf, x, value):
    uf['weight'][x] = value

def increment_weight(uf, x, value):
    uf['weight'][x] += value

def get_added(uf, x):
    return uf['added'][x]

def increment_added(uf, x, value):
    uf['added'][x] += value

def find(uf, x):
    if get_parent(uf, x) == x:
        return x
    updated_parent = find(uf, get_parent(uf, x))
    update_weight_on_find(uf, x)
    set_parent(uf, x, updated_parent)
    return updated_parent

def update_weight_on_find(uf, x):
    increment_weight(uf, x, get_weight(uf, get_parent(uf, x)))

def diff(uf, x, y):
    temp = (get_weight(uf, x) - get_weight(uf, y) 
            + get_added(uf, x) - get_added(uf, y))
    return temp

def union(uf, x, y, w):
    rx = find(uf, x)
    ry = find(uf, y)
    increment_added(uf, x, w)
    increment_added(uf, y, w)
    u_rank = get_rank(uf, rx)
    v_rank = get_rank(uf, ry)
    if u_rank < v_rank:
        set_parent(uf, rx, ry)
        set_weight(uf, rx, w - diff(uf, x, y))
    else:
        set_parent(uf, ry, rx)
        set_weight(uf, ry, -w + diff(uf, x, y))
        if u_rank == v_rank:
            increment_rank(uf, rx)

def same(uf, x, y):
    return find(uf, x) == find(uf, y)

def added_diff(uf, x, y):
    return diff(uf, x, y)

def parse_input():
    return list(map(int, input().split()))

def parse_line(line):
    parts = line.strip().split()
    return parts[0], parts[1:]

def process_input_line_for_dealin(uf, l):
    a, b, c = map(int, l)
    union(uf, b, a, c)

def process_input_line_for_compare(uf, l):
    a, b = map(int, l)
    if same(uf, a, b):
        return added_diff(uf, b, a)
    else:
        return "WARNING"

def print_ans(ans_list):
    print("\n".join(map(str, ans_list)))

def main_loop(N, Q):
    uf = initialize_weighted_union_find(N + 1)
    ans = []
    for _ in range(Q):
        s, *l = input().split()
        if s == "IN":
            process_input_line_for_dealin(uf, l)
        else:
            ret = process_input_line_for_compare(uf, l)
            ans.append(ret)
    if ans:
        print_ans(ans)

def initial_setup_and_execute():
    N_Q = input().split()
    N, Q = int(N_Q[0]), int(N_Q[1])
    main_loop(N, Q)

initial_setup_and_execute()