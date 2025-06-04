def read_input():
    return raw_input()

def parse_input_line(line):
    return map(int, line.split())

def is_end_of_input(N):
    return N == 0

def read_data_rows(N):
    rows = []
    for i in range(N):
        rows.append(raw_input().split())
    return rows

def convert_data_types(dat):
    for i in range(len(dat)):
        dat[i][1] = int(dat[i][1])
        dat[i][2] = int(dat[i][2])
    return dat

def sort_data(dat):
    return sorted(dat, key=lambda x: x[2])

def compute_mid(l, r):
    return l + (r - l) / 2

def is_same_index(l, r):
    return l == r

def get_query_value():
    return int(raw_input())

def should_return_left(q, dat, l):
    return q <= dat[l][2]

def should_search_left(q, dat, l, r):
    return q <= dat[compute_mid(l, r)][2]

def should_search_right(q, dat, l, r):
    return dat[compute_mid(l, r)][2] < q

def bm_search_recursive(dat, q, l, r):
    if is_same_index(l, r):
        if should_return_left(q, dat, l):
            return int(l)
        else:
            return l + 1
    elif should_search_left(q, dat, l, r):
        return bm_search_recursive(dat, q, l, compute_mid(l, r))
    elif should_search_right(q, dat, l, r):
        return bm_search_recursive(dat, q, compute_mid(l, r) + 1, r)

def bm_search(dat, q, l, r):
    return bm_search_recursive(dat, q, l, r)

def can_compute_result(p, N):
    return p < N

def is_valid_result(dat, p, q):
    return dat[p][1] > dat[p][2] - q

def compute_result(dat, p, q):
    name = dat[p][0]
    value = dat[p][1] - (dat[p][2] - q)
    return name, value

def print_result(name, value):
    print name, value

def print_unknown():
    print "Unknown"

def process_queries(Q, N, dat):
    for i in range(Q):
        q = get_query_value()
        p = bm_search(dat, q, 0, N - 1)
        if can_compute_result(p, N) and is_valid_result(dat, p, q):
            name, value = compute_result(dat, p, q)
            print_result(name, value)
        else:
            print_unknown()

def main_loop():
    while True:
        N_Q_line = read_input()
        N, Q = parse_input_line(N_Q_line)
        if is_end_of_input(N):
            break
        dat = read_data_rows(N)
        dat = convert_data_types(dat)
        dat = sort_data(dat)
        process_queries(Q, N, dat)

main_loop()