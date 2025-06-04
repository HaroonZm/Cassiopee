import math

def read_input():
    return float(raw_input())

def compute_initial_answer(d):
    return math.sqrt(2) * d

def get_range():
    return xrange(1, 11)

def compute_lower_bound(x):
    return x * x

def compute_upper_bound(x):
    return x * 2 + 1

def condition(d, x):
    return compute_lower_bound(x) <= d * d <= compute_upper_bound(x)

def update_answer(ans, x):
    return max(ans, x + 1)

def format_output(ans):
    return "%.10f" % ans

def main():
    d = read_input()
    ans = compute_initial_answer(d)
    for x in get_range():
        if condition(d, x):
            ans = update_answer(ans, x)
    print format_output(ans)

main()