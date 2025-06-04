from collections import deque

def read_n_and_q():
    return list(map(int, input().split()))

def build_list_of_deques(n):
    return [deque() for _ in range(n)]

def parse_query(q):
    return input()

def insert_query(query, L):
    _, t, x = list(map(int, query.split()))
    L[t].append(x)

def dump_query(query, L):
    _, t = list(map(int, query.split()))
    print(*L[t])

def should_insert(query):
    return query[0] == "0"

def should_dump(query):
    return query[0] == "1"

def should_splice(query):
    return not (should_insert(query) or should_dump(query))

def parse_splice_args(query):
    _, s, t = list(map(int, query.split()))
    return s, t

def handle_empty_target(L, s, t):
    L[t] = L[s]

def handle_singleton_source(L, s, t):
    L[t].append(L[s][0])

def handle_singleton_target(L, s, t):
    L[s].appendleft(L[t][0])
    L[t] = L[s]

def handle_extend(L, s, t):
    L[t].extend(L[s])

def handle_splice(L, s, t):
    if not L[t]:
        handle_empty_target(L, s, t)
    elif len(L[s]) == 1:
        handle_singleton_source(L, s, t)
    elif len(L[t]) == 1:
        handle_singleton_target(L, s, t)
    else:
        handle_extend(L, s, t)
    L[s] = deque()

def handle_query(query, L):
    if should_insert(query):
        insert_query(query, L)
    elif should_dump(query):
        dump_query(query, L)
    elif should_splice(query):
        s, t = parse_splice_args(query)
        handle_splice(L, s, t)

def main_loop(n, q, L):
    for _ in range(q):
        query = parse_query(q)
        handle_query(query, L)

def main():
    n, q = read_n_and_q()
    L = build_list_of_deques(n)
    main_loop(n, q, L)

main()