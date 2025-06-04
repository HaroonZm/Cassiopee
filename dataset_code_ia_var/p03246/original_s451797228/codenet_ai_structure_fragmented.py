def read_input():
    return int(input())

def read_values():
    return list(map(int, input().split()))

def create_empty_dict():
    return {}

def update_dict_count(d, v):
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1

def process_even_indices(V, v1):
    for v in V[::2]:
        update_dict_count(v1, v)

def process_odd_indices(V, v2):
    for v in V[1::2]:
        update_dict_count(v2, v)

def get_sorted_keys_by_values(d):
    return sorted(d, key=lambda x: -d[x])

def get_top_keys(a, count):
    return a[:count]

def add_result_if_distinct(r, k1, k2, N, v1, v2):
    if k1 != k2:
        r.append(N - v1[k1] - v2[k2])

def ensure_result_non_empty(r, N):
    if not r:
        r.append(N // 2)

def compute_min_result(r):
    return min(r)

def main_logic():
    N = read_input()
    V = read_values()
    
    v1 = create_empty_dict()
    v2 = create_empty_dict()
    
    process_even_indices(V, v1)
    process_odd_indices(V, v2)
    
    a1 = get_sorted_keys_by_values(v1)
    a2 = get_sorted_keys_by_values(v2)
    
    r = []
    top_a1 = get_top_keys(a1, 2)
    top_a2 = get_top_keys(a2, 2)
    for k1 in top_a1:
        for k2 in top_a2:
            add_result_if_distinct(r, k1, k2, N, v1, v2)
    
    ensure_result_non_empty(r, N)
    
    print(compute_min_result(r))

main_logic()