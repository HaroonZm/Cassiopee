import sys
sys.setrecursionlimit(100000)

def shift_right(value):
    return value >> 1

def is_zero(value):
    return value == 0

def bit_and_one(value):
    return value & 1

def bitwise_or_three(a, b, c):
    return a | b | c

def toC_base_case(A, B):
    return 0 if not (A or B) else None

def toC_case_c_odd(A, B, C):
    if bit_and_one(C):
        return toC(shift_right(A), shift_right(B), shift_right(C))
    return None

def toC_case_b_odd(A, B, C):
    if bit_and_one(B):
        part1 = toC(shift_right(C), shift_right(B), shift_right(A))
        part2 = toC(shift_right(bitwise_or_three(A, B, C)), 0, 0)
        return part1 + part2 + 1
    return None

def toC_case_a_odd(A, B, C):
    if bit_and_one(A):
        part1 = toC(shift_right(A), shift_right(B), shift_right(C))
        part2 = toC(shift_right(bitwise_or_three(A, B, C)), 0, 0)
        return part1 + 2 * part2 + 2
    return None

def toC(A, B, C):
    base = toC_base_case(A, B)
    if base is not None:
        return base
    res = toC_case_c_odd(A, B, C)
    if res is not None:
        return res
    res = toC_case_b_odd(A, B, C)
    if res is not None:
        return res
    res = toC_case_a_odd(A, B, C)
    if res is not None:
        return res

def read_line_of_ints():
    return list(map(int, input().split()))

def read_cups_line():
    line = read_line_of_ints()
    return line[1:]

def cups_to_bits(cup_list):
    bits = 0
    for s in cup_list:
        bits |= 1 << (s - 1)
    return bits

def read_cups():
    cups_bits = []
    for _ in range(3):
        cup = read_cups_line()
        bits = cups_to_bits(cup)
        cups_bits.append(bits)
    return cups_bits

def process_single_case(n, m):
    cups = read_cups()
    result = min(toC(*cups), toC(*cups[::-1]))
    if result <= m:
        print(result)
    else:
        print(-1)

def resolve():
    while True:
        n, m = read_line_of_ints()
        if n == 0:
            return
        process_single_case(n, m)

if __name__ == "__main__":
    resolve()