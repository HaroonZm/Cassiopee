from bisect import bisect_left, bisect_right, insort_left

def read_query_count():
    return int(input())

def read_query():
    return list(input().split())

def insert_key(keytbl, d, ki, val):
    add_key_if_not_exists(keytbl, d, ki)
    d[ki] = val

def add_key_if_not_exists(keytbl, d, ki):
    if ki not in d:
        insort_left(keytbl, ki)

def print_key_value(d, ki):
    print(d[ki] if ki in d else 0)

def set_key_zero(d, ki):
    if ki in d:
        d[ki] = 0

def handle_range_query(keytbl, d, left_key, right_key):
    L = get_left_idx(keytbl, left_key)
    R = get_right_idx(keytbl, left_key, right_key, L)
    for j in range(L, R):
        check_and_print_positive(keytbl, d, j)

def get_left_idx(keytbl, left_key):
    return bisect_left(keytbl, left_key)

def get_right_idx(keytbl, left_key, right_key, L):
    return bisect_right(keytbl, right_key, L)

def check_and_print_positive(keytbl, d, idx):
    key = keytbl[idx]
    if d[key] > 0:
        print(key, d[key])

def process_queries(q):
    d = {}
    keytbl = []
    for _ in range(q):
        a = read_query()
        process_single_query(a, d, keytbl)

def process_single_query(a, d, keytbl):
    operation = a[0]
    ki = a[1]
    if operation == "0":
        insert_key(keytbl, d, ki, int(a[2]))
    elif operation == "1":
        print_key_value(d, ki)
    elif operation == "2":
        set_key_zero(d, ki)
    else:
        handle_range_query(keytbl, d, a[1], a[2])

def main():
    q = read_query_count()
    process_queries(q)

main()