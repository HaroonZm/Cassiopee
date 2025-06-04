def read_query_count():
    return int(input())

def read_query():
    return list(map(int, input().split()))

def append_to_list(A, value):
    A.append(value)

def print_from_list(A, index):
    print(A[index])

def pop_from_list(A):
    A.pop(-1)

def handle_query(query, A):
    if is_append_query(query):
        handle_append_query(query, A)
    elif is_print_query(query):
        handle_print_query(query, A)
    else:
        handle_pop_query(A)

def is_append_query(query):
    return query[0] == 0

def is_print_query(query):
    return query[0] == 1

def handle_append_query(query, A):
    append_to_list(A, query[1])

def handle_print_query(query, A):
    print_from_list(A, query[1])

def handle_pop_query(A):
    pop_from_list(A)

def process_queries(q):
    A = []
    for _ in range(q):
        query = read_query()
        handle_query(query, A)

def main():
    q = read_query_count()
    process_queries(q)

main()