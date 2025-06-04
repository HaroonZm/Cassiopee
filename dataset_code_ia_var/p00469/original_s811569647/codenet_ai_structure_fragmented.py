import itertools

def read_input():
    return raw_input()

def should_terminate_input(n):
    return n == "0 0"

def parse_n_k(n_input):
    parts = n_input.split()
    n = int(parts[0])
    return n

def read_k():
    return input()

def should_terminate_k(k):
    return k == 0

def read_lines(n):
    return [raw_input() for _ in range(n)]

def generate_permutations(L, k):
    return itertools.permutations(L, k)

def join_tuple(t):
    return "".join(t)

def add_to_set(S, s):
    S.add(s)

def print_length(S):
    print len(S)

def process_case(n_input):
    n = parse_n_k(n_input)
    k = read_k()
    if should_terminate_k(k):
        return False
    L = read_lines(n)
    S = set()
    for t in generate_permutations(L, k):
        s = join_tuple(t)
        add_to_set(S, s)
    print_length(S)
    return True

def main_loop():
    while True:
        n_input = read_input()
        if should_terminate_input(n_input):
            break
        cont = process_case(n_input)
        if not cont:
            break

main_loop()