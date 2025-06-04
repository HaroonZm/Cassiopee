def read_input():
    return input()

def parse_n_m(line):
    return map(int, line.split())

def init_used(n):
    return [1] + [0] * n

def read_src(m):
    return [int(read_input()) for _ in range(m)]

def process_src(src):
    return reversed(src)

def check_used(used, v):
    return used[v]

def mark_used(used, v):
    used[v] = 1

def print_value(v):
    print(v)

def process_used_reversed(src, used):
    iterator = process_src(src)
    for v in iterator:
        if check_used(used, v):
            continue
        print_value(v)
        mark_used(used, v)

def enumerate_used(used):
    return enumerate(used)

def process_unused(used):
    for v, u in enumerate_used(used):
        if not u:
            print_value(v)

def main():
    line = read_input()
    n, m = parse_n_m(line)
    used = init_used(n)
    src = read_src(m)
    process_used_reversed(src, used)
    process_unused(used)

main()