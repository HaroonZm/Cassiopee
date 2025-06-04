import sys

def read_input():
    n, m = map(int, input().split())
    binary_rows = []
    for line in sys.stdin:
        b = ''.join(line.rstrip().split())
        binary_rows.append(int(b, base=2))
    return n, m, binary_rows

def find_max(rows):
    if not rows:
        return 0
    return max(rows)

def bit_length_minus_one(x):
    return x.bit_length() - 1

def get_highest_bit_mask(x):
    return 1 << bit_length_minus_one(x)

def is_not_zero(x):
    return x != 0

def transform_rows(rows, x, y):
    new_rows = []
    for r in rows:
        if r == x:
            continue
        if r & y:
            new_rows.append(r ^ x)
        else:
            new_rows.append(r)
    return new_rows

def count_independent_rows(rows):
    independent_row = 0
    current_rows = rows.copy()
    while current_rows:
        x = find_max(current_rows)
        if x == 0:
            break
        if is_not_zero(x):
            independent_row += 1
        y = get_highest_bit_mask(x)
        current_rows = transform_rows(current_rows, x, y)
    return independent_row

def power_of_two(exp, mod):
    return pow(2, exp, mod)

def subtract_and_mod(a, b, mod):
    return (a - b) % mod

def compute_answer(n, m, independent_row, mod):
    exp1 = n + m - 1
    exp2 = n + m - independent_row - 1
    val1 = power_of_two(exp1, mod)
    val2 = power_of_two(exp2, mod)
    return subtract_and_mod(val1, val2, mod)

def main():
    MOD = 998244353
    n, m, rows = read_input()
    independent_row = count_independent_rows(rows)
    ans = compute_answer(n, m, independent_row, MOD)
    print(ans)

main()