from collections import deque
import sys

def read_initial_inputs():
    return map(int, input().split())

def create_queues(n):
    return [deque() for _ in range(n)]

def process_queries(Q):
    for query in (line.split() for line in sys.stdin):
        handle_single_query(Q, query)

def handle_single_query(Q, query):
    op_type = query_type(query)
    if op_type == 0:
        process_append(Q, query)
    elif op_type == 1:
        process_print(Q, query)
    elif op_type == 2:
        process_merge(Q, query)

def query_type(query):
    return int(query[0])

def get_s(query):
    return int(query[1])

def get_t(query):
    return int(query[2])

def process_append(Q, query):
    s = get_s(query)
    t = get_t(query)
    append_to_queue(Q, s, t)

def append_to_queue(Q, s, t):
    Q[s].append(t)

def process_print(Q, query):
    s = get_s(query)
    print_queue(Q, s)

def print_queue(Q, s):
    print(*Q[s])

def process_merge(Q, query):
    s = get_s(query)
    t = get_t(query)
    merge_queues(Q, s, t)

def merge_queues(Q, s, t):
    if queue_exists(Q, t):
        handle_non_empty_target(Q, s, t)
    else:
        handle_empty_target(Q, s, t)
    clear_source_queue(Q, s)

def queue_exists(Q, index):
    return bool(Q[index])

def handle_non_empty_target(Q, s, t):
    if is_singleton(Q, s):
        append_first(Q, t, get_first(Q, s))
    elif is_singleton(Q, t):
        prepend_first(Q, s, get_first(Q, t))
        assign_queue(Q, t, Q[s])
    else:
        extend_queue(Q, t, Q[s])

def is_singleton(Q, index):
    return len(Q[index]) == 1

def get_first(Q, index):
    return Q[index][0]

def append_first(Q, t, val):
    Q[t].append(val)

def prepend_first(Q, s, val):
    Q[s].appendleft(val)

def assign_queue(Q, t, source):
    Q[t] = source

def extend_queue(Q, t, source):
    Q[t].extend(source)

def handle_empty_target(Q, s, t):
    assign_queue(Q, t, Q[s])

def clear_source_queue(Q, s):
    Q[s] = deque()

def main():
    n, q = read_initial_inputs()
    Q = create_queues(n)
    process_queries(Q)

main()