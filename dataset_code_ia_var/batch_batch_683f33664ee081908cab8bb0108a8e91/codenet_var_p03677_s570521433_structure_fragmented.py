import sys

def get_input():
    return sys.stdin.readline

def parse_first_line(input_func):
    return map(int, input_func().split())

def parse_second_line(input_func):
    return list(map(lambda x: int(x) - 1, input_func().split()))

def construct_BIT(size):
    return BIT(size)

def update_sum(bit, i):
    return bit.sum(i)

def update_add(bit, i, x):
    bit.add(i, x)

def handle_case_cont(bit0, bit1, x, y):
    return

def handle_case_normal(bit0, bit1, x, y, m):
    x2 = (x + 2) % m
    update_add(bit0, x2, -1)
    update_add(bit1, x2, x2 - 1)
    update_add(bit0, y + 1, 1)
    update_add(bit1, y + 1, -(x2 - 1))

def handle_case_wraparound(bit0, bit1, x, y, m):
    x2 = (x + 2) % m
    update_add(bit0, x2, -1)
    update_add(bit1, x2, x2 - 1)
    b = (0 - (x2 - 1)) % m
    update_add(bit0, 0, -1)
    update_add(bit1, 0, -b)
    update_add(bit0, y + 1, 1)
    update_add(bit1, y + 1, b)

def process_pair(bit0, bit1, a, i, m):
    x, y = a[i], a[i+1]
    update_add(bit1, 0, (y - x) % m)
    if (y - x) % m < 2:
        handle_case_cont(bit0, bit1, x, y)
        return
    x2 = (x + 2) % m
    if x2 <= y:
        handle_case_normal(bit0, bit1, x, y, m)
    else:
        handle_case_wraparound(bit0, bit1, x, y, m)

def process_all_pairs(bit0, bit1, a, n, m):
    for i in range(n - 1):
        process_pair(bit0, bit1, a, i, m)

def calculate_value(bit0, bit1, i):
    return update_sum(bit0, i) * i + update_sum(bit1, i)

def solve_min(bit0, bit1, m):
    candidates = []
    for i in range(m):
        candidates.append(calculate_value(bit0, bit1, i))
    return min(candidates)

def main():
    input_func = get_input()
    n, m = parse_first_line(input_func)
    a = parse_second_line(input_func)
    bit0 = construct_BIT(m)
    bit1 = construct_BIT(m)
    process_all_pairs(bit0, bit1, a, n, m)
    ans = solve_min(bit0, bit1, m)
    print(ans)

class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)
        self.size = size

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

main()