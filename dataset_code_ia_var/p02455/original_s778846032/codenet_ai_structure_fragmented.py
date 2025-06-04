def read_query_count():
    return int(input())

def init_set():
    return set()

def read_operation():
    return map(int, input().split())

def is_add_operation(op):
    return op == 0

def perform_add_operation(se, x):
    se.add(x)
    return len(se)

def perform_query_operation(se, x):
    return int(x in se)

def print_result(result):
    print(result)

def decrement_counter(q):
    return q - 1

def main_loop(q, se):
    while continue_loop(q):
        q = decrement_counter(q)
        op, x = read_operation()
        if is_add_operation(op):
            res = perform_add_operation(se, x)
            print_result(res)
        else:
            res = perform_query_operation(se, x)
            print_result(res)

def continue_loop(q):
    return q > 0

def main():
    q = read_query_count()
    se = init_set()
    main_loop(q, se)

main()