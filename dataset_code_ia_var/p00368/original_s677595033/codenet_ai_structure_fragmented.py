def read_inputs():
    w, h = map(int, input().split())
    base = list(map(int, input().split()))
    return w, h, base

def count_zeros(lst):
    return lst.count(0)

def check_zero_balance(w, base):
    num_zeros = count_zeros(base)
    return abs(2 * num_zeros - w) < 2

def parse_line():
    return list(map(int, input().split()))

def is_first_item_same(line1, line2):
    return line1[0] == line2[0]

def lines_are_equal(line1, line2):
    return line1 == line2

def have_any_same_column(line1, line2):
    return any(i == j for i, j in zip(line1, line2))

def check_non_diff_line(line, base):
    if lines_are_equal(line, base):
        return True
    return False

def check_diff_line(line, base):
    return not have_any_same_column(line, base)

def process_lines(h, base):
    same = 1
    for _ in range(h - 1):
        line = parse_line()
        flag = is_first_item_same(base, line)
        same += flag
        if flag:
            if not check_non_diff_line(line, base):
                return None  # Early exit: invalid
        else:
            if not check_diff_line(line, base):
                return None  # Early exit: invalid
    return same

def good_same_balance(same, h):
    return abs(2 * same - h) <= 1

def solve():
    w, h, base = read_inputs()
    if not check_zero_balance(w, base):
        return False
    same = process_lines(h, base)
    if same is None:
        return False
    return good_same_balance(same, h)

print("yes" if solve() else "no")