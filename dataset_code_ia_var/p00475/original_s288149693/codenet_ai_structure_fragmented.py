import sys
from sys import stdin

def read_input_line():
    return stdin.readline()

def parse_int(line):
    return int(line)

def parse_point(line):
    a, b = map(int, line.split())
    return a, b

def transform_point(a, b):
    return a + b, a - b

def collect_points(n):
    x = []
    y = []
    for _ in range(n):
        line = read_input_line()
        a, b = parse_point(line)
        xp, yp = transform_point(a, b)
        x.append(xp)
        y.append(yp)
    return x, y

def find_min(arr):
    return min(arr)

def find_max(arr):
    return max(arr)

def compute_extrema(x, y):
    xmin = find_min(x)
    xmax = find_max(x)
    ymin = find_min(y)
    ymax = find_max(y)
    return xmin, xmax, ymin, ymax

def single_d1(i, x, y, xmin, ymin):
    return max(x[i] - xmin, y[i] - ymin)

def single_d2(i, x, y, xmax, ymax):
    return max(xmax - x[i], ymax - y[i])

def alternative_d1(i, x, y, xmin, ymax):
    return max(x[i] - xmin, ymax - y[i])

def alternative_d2(i, x, y, xmax, ymin):
    return max(xmax - x[i], y[i] - ymin)

def calc_ans1(n, x, y, xmin, xmax, ymin, ymax):
    ans1 = 0
    for i in range(n):
        d1 = single_d1(i, x, y, xmin, ymin)
        d2 = single_d2(i, x, y, xmax, ymax)
        ans1 = max(ans1, min(d1, d2))
    return ans1

def calc_ans2(n, x, y, xmin, xmax, ymin, ymax):
    ans2 = 0
    for i in range(n):
        d1 = alternative_d1(i, x, y, xmin, ymax)
        d2 = alternative_d2(i, x, y, xmax, ymin)
        ans2 = max(ans2, min(d1, d2))
    return ans2

def output_result(ans1, ans2):
    print(min(ans1, ans2))

def main():
    n_line = read_input_line()
    n = parse_int(n_line)
    x, y = collect_points(n)
    xmin, xmax, ymin, ymax = compute_extrema(x, y)
    ans1 = calc_ans1(n, x, y, xmin, xmax, ymin, ymax)
    ans2 = calc_ans2(n, x, y, xmin, xmax, ymin, ymax)
    output_result(ans1, ans2)

main()