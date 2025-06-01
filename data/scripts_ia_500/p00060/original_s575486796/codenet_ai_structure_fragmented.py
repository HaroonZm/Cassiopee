import sys
def get_input_lines():
    return sys.stdin.readlines()

def initialize_U():
    return [0]*11

def parse_line(line):
    return map(int, line.split())

def mark_positions(U, a, b, c):
    U[a] = 1
    U[b] = 1
    U[c] = 1

def is_position_marked(U, x):
    return U[x] == 1

def sum_values(a, b, x):
    return a + b + x

def should_count(a, b, x):
    return sum_values(a, b, x) <= 20

def count_valid_positions(U, a, b):
    count = 0
    for x in range(1, 11):
        if is_position_marked(U, x):
            continue
        if should_count(a, b, x):
            count += 1
    return count

def decide_result(count):
    if count * 2 > 7:
        return "YES\n"
    else:
        return "NO\n"

def solve():
    lines = get_input_lines()
    write = sys.stdout.write
    for line in lines:
        U = initialize_U()
        a, b, c = parse_line(line)
        mark_positions(U, a, b, c)
        count = count_valid_positions(U, a, b)
        result = decide_result(count)
        write(result)

solve()