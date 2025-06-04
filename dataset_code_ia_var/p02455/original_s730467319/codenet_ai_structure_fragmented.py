def read_n():
    return int(input())

def read_query():
    return map(int, input().split())

def init_set():
    return set()

def add_to_set(s, x):
    s.add(x)

def check_in_set(s, x):
    return x in s

def print_len(s):
    print(len(s))

def print_one():
    print(1)

def print_zero():
    print(0)

def make_singleton_set(x):
    return {x}

def handle_query_zero(S, x):
    if check_in_set(S, x):
        print_len(S)
    else:
        add_to_set(S, x)
        print_len(S)

def handle_query_one(S, x):
    singleton = make_singleton_set(x)
    if S >= singleton:
        print_one()
    else:
        print_zero()

def process_query(S, q, x):
    if q == 0:
        handle_query_zero(S, x)
    else:
        handle_query_one(S, x)

def main():
    S = init_set()
    n = read_n()
    for _ in range(n):
        q, x = read_query()
        process_query(S, q, x)

main()