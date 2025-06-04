from sys import stdout

def read_initial_input():
    return int(raw_input())

def request_input(b):
    print_first_line(b)
    print_second_line(b)
    flush_output()
    return read_response()

def print_first_line(b):
    print b[0]

def print_second_line(b):
    print b[1]

def flush_output():
    stdout.flush()

def read_response():
    return raw_input().strip()

def get_patterns():
    return ['..', '.#', '#.', '##']

def initialize_states():
    return ['', '']

def build_candidate_a(a, t):
    return [a[0] + t[0], a[1] + t[1]]

def build_candidate_b(a, t):
    return [t[0] + a[0], t[1] + a[1]]

def process_first_phase(a, patterns):
    while True:
        if iterate_first_phase(a, patterns):
            break

def iterate_first_phase(a, patterns):
    for t in patterns:
        b = build_candidate_a(a, t)
        r = request_input(b)
        if is_end(r):
            terminate_program()
        if is_target(r):
            update_state(a, b)
            return False
    return True

def process_second_phase(a, patterns):
    while True:
        if iterate_second_phase(a, patterns):
            break

def iterate_second_phase(a, patterns):
    for t in patterns:
        b = build_candidate_b(a, t)
        r = request_input(b)
        if is_end(r):
            terminate_program()
        if is_target(r):
            update_state(a, b)
            return False
    return True

def is_end(response):
    return response == 'end'

def is_target(response):
    return response == 'T'

def terminate_program():
    quit()

def update_state(a, b):
    a[0] = b[0]
    a[1] = b[1]

def main():
    n = read_initial_input()
    patterns = get_patterns()
    a = initialize_states()
    process_first_phase(a, patterns)
    process_second_phase(a, patterns)

main()