import math

def get_buffer_length(buff):
    return len(buff)

def sum_buffer(buff):
    return sum(buff)

def convert_sum_to_float(s):
    return float(s)

def calculate_mean(s, n):
    return s / n

def calculate_diff(x, m):
    return x - m

def square_value(a):
    return a * a

def accumulate_squares(buff, m):
    s1 = 0.0
    for x in buff:
        a = calculate_diff(x, m)
        s1 += square_value(a)
    return s1

def divide_sum(s1, n):
    return s1 / n

def square_root(val):
    return math.sqrt(val)

def mean_sd(buff):
    n = get_buffer_length(buff)
    s = sum_buffer(buff)
    f_s = convert_sum_to_float(s)
    m = calculate_mean(f_s, n)
    s1 = accumulate_squares(buff, m)
    d = divide_sum(s1, n)
    res = square_root(d)
    return res

def read_line():
    return raw_input()

def should_exit(line):
    return line == "0"

def parse_floats(line):
    return map(float, line.split(" "))

def print_result(res):
    print res

def main():
    while True:
        line = read_line()
        if should_exit(line):
            break
        nums_line = read_line()
        x = parse_floats(nums_line)
        res = mean_sd(x)
        print_result(res)

main()