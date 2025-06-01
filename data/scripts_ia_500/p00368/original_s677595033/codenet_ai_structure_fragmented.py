def read_dimensions():
    return map(int, input().split())

def read_line():
    return list(map(int, input().split()))

def count_zeroes(line):
    return line.count(0)

def check_zero_balance(zero_count, width):
    return abs(2 * zero_count - width) < 2

def lines_are_equal(line1, line2):
    return line1 == line2

def first_elements_equal(line1, line2):
    return line1[0] == line2[0]

def any_elements_equal(line1, line2):
    return any(i == j for i, j in zip(line1, line2))

def update_same_count(same_count, condition):
    return same_count + condition

def check_same_balance(same_count, height):
    return abs(2 * same_count - height) <= 1

def solve():
    w, h = read_dimensions()
    base = read_line()
    zero_count = count_zeroes(base)
    if not check_zero_balance(zero_count, w):
        return False
    same = 1
    for _ in range(h - 1):
        line = read_line()
        flag = first_elements_equal(base, line)
        same = update_same_count(same, flag)
        if flag:
            if not lines_are_equal(line, base):
                return False
        else:
            if any_elements_equal(line, base):
                return False
    return check_same_balance(same, h)

def main():
    result = solve()
    output = "yes" if result else "no"
    print(output)

main()