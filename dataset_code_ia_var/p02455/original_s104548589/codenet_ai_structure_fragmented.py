def read_query_count():
    return int(input())

def initialize_set():
    return set([])

def process_queries(q, S):
    for i in range(q):
        query, x = read_query()
        handle_query(query, x, S)

def read_query():
    inputs = input().split()
    return parse_query(inputs)

def parse_query(inputs):
    query = int(inputs[0])
    x = int(inputs[1])
    return query, x

def handle_query(query, x, S):
    if is_insert_query(query):
        handle_insert(x, S)
    else:
        handle_find(x, S)

def is_insert_query(query):
    return query == 0

def handle_insert(x, S):
    add_to_set(x, S)
    print_set_length(S)

def add_to_set(x, S):
    S.add(x)

def print_set_length(S):
    print(len(S))

def handle_find(x, S):
    if is_in_set(x, S):
        print_found()
    else:
        print_not_found()

def is_in_set(x, S):
    return x in S

def print_found():
    print(1)

def print_not_found():
    print(0)

def main():
    q = read_query_count()
    S = initialize_set()
    process_queries(q, S)

main()