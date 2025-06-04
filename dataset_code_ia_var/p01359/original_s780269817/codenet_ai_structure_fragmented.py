import bisect

def read_N_Q():
    return map(int, input().split())

def should_terminate(N):
    return N == 0

def read_src_entry():
    n, l, y = input().split()
    return (int(y), int(l), n)

def read_src_entries(N):
    entries = []
    for _ in range(N):
        entry = read_src_entry()
        entries.append(entry)
    return entries

def sort_src(src):
    src.sort()

def read_query():
    return int(input())

def process_query(q, src, N):
    pos = bisect.bisect(src, (q, -1, -1))
    if check_valid(pos, src, N, q):
        print_valid(pos, src, q)
        return
    if check_valid(pos + 1, src, N, q):
        print_valid(pos + 1, src, q)
        return
    print_unknown()

def check_valid(a, src, N, q):
    if a < N:
        y, l, n = src[a]
        return y - l < q <= y
    return False

def print_valid(a, src, q):
    y, l, n = src[a]
    print(n + ' ' + str(q - y + l))

def print_unknown():
    print('Unknown')

def process_entries(N, Q, src):
    for _ in range(Q):
        q = read_query()
        process_query(q, src, N)

def process_once():
    N, Q = read_N_Q()
    if should_terminate(N):
        return False
    src = read_src_entries(N)
    sort_src(src)
    process_entries(N, Q, src)
    return True

def main_loop():
    while True:
        if not process_once():
            break

main_loop()