def read_int():
    return int(input())

def read_query():
    return list(map(int, input().split()))

def handle_append(v, value):
    v.append(value)

def handle_print(v, index):
    print(v[index])

def handle_pop(v):
    v.pop()

def process_query(query, v):
    op = query[0]
    if op == 0:
        handle_append(v, query[1])
    elif op == 1:
        handle_print(v, query[1])
    elif op == 2:
        handle_pop(v)

def main_loop(q_count, v):
    def run_iteration(_):
        query = read_query()
        process_query(query, v)
    list(map(run_iteration, range(q_count)))

def main():
    q_count = read_int()
    v = []
    main_loop(q_count, v)

main()