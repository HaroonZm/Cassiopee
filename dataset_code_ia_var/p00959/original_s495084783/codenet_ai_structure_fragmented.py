def read_input():
    return raw_input()

def parse_input_line(line):
    return map(int, line.split())

def get_next_value():
    return input()

def update_max(current_max, value):
    return max(current_max, value)

def compute_remaining(t, accumulated):
    return t - accumulated

def check_negative(remaining):
    return remaining < 0

def compute_initial_answer(remaining, max_value):
    return remaining / max_value + 1

def check_remainder(remaining, max_value, current):
    return (remaining % max_value) >= current

def print_one():
    print 1

def print_answer(ans):
    print ans

def main():
    input_line = read_input()
    n, t = parse_input_line(input_line)
    mx = 0
    s = 0
    for i in xrange(n):
        x = get_next_value()
        mx = update_max(mx, x)
        r = compute_remaining(t, s)
        if check_negative(r):
            print_one()
        else:
            ans = compute_initial_answer(r, mx)
            if check_remainder(r, mx, x):
                ans += 1
            print_answer(ans)
        s += x

main()