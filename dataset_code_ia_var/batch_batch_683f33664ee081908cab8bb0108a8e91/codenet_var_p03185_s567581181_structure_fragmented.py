import sys
from collections import deque

def read_input():
    return sys.stdin.readline().strip()

def parse_first_line():
    return map(int, read_input().split())

def parse_heights():
    return list(map(int, read_input().split()))

def init_deque():
    return deque()

def create_line(a, b):
    return (a, b)

def cross_product(f1, f2, f3):
    x1 = f2[0] - f1[0]
    x2 = f3[1] - f2[1]
    y1 = f2[1] - f1[1]
    y2 = f3[0] - f2[0]
    return x1 * x2 >= y1 * y2

def line_value(f, x):
    return f[0]*x + f[1]

def remove_last_line_if_needed(que, fi):
    while len(que) >= 2 and cross_product(que[-2], que[-1], fi):
        que.pop()

def add_line_to_deque(que, a, b):
    fi = create_line(a, b)
    remove_last_line_if_needed(que, fi)
    que.append(fi)

def remove_first_line_if_needed(que, x):
    while len(que) >= 2 and line_value(que[0], x) >= line_value(que[1], x):
        que.popleft()

def query_deque(que, x):
    remove_first_line_if_needed(que, x)
    return line_value(que[0], x)

def initialize_DP(n):
    return [0]*n

def main():
    n, c = parse_first_line()
    h = parse_heights()
    cht_deque = init_deque()
    add_line_to_deque(cht_deque, -2*h[0], h[0]*h[0])
    DP = initialize_DP(n)
    for i in range(1, n):
        min_cost = query_deque(cht_deque, h[i])
        DP[i] = min_cost + h[i]*h[i] + c
        add_line_to_deque(cht_deque, -2*h[i], h[i]*h[i] + DP[i])
    print(DP[-1])

if __name__ == "__main__":
    main()