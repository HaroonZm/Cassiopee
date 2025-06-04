from bisect import bisect_left, bisect_right, insort_left

def get_query_count():
    return int(input())

def read_query():
    return list(input().split())

def read_queries(q):
    queries = []
    for _ in range(q):
        queries.append(read_query())
    return queries

def insert_or_update(S, W, key, value):
    if key not in S:
        insort_left(W, key)
    S[key] = int(value)

def print_value(S, key):
    if key in S:
        print(S[key])
    else:
        print(0)

def reset_value(S, key):
    if key in S:
        S[key] = 0

def process_interval_query(S, W, left, right):
    l_index = bisect_left(W, left)
    r_index = bisect_right(W, right)
    for i in range(l_index, r_index):
        if S[W[i]] > 0:
            print(W[i], S[W[i]])

def process_single_query(S, W, query):
    if query[0] == '0':
        insert_or_update(S, W, query[1], query[2])
    elif query[0] == '1':
        print_value(S, query[1])
    elif query[0] == '2':
        reset_value(S, query[1])
    else:
        process_interval_query(S, W, query[1], query[2])

def process_queries(queries):
    S = {}
    W = []
    for query in queries:
        process_single_query(S, W, query)

def main():
    q = get_query_count()
    queries = read_queries(q)
    process_queries(queries)

main()