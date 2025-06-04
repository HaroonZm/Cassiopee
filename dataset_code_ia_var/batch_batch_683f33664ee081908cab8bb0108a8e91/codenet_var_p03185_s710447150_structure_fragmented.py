from collections import deque

def main():
    N, C, hs = read_input()
    result = compute_min_cost(N, C, hs)
    print(result)

def read_input():
    N, C = map(int, input().split())
    hs = list(map(int, input().split()))
    return N, C, hs

def compute_min_cost(N, C, hs):
    cht = create_convex_hull_trick()
    dp = initialize_dp(N)
    for i in range(1, N):
        add_line_to_cht(cht, hs, dp, i)
        min_value = query_min_value(cht, hs[i])
        dp[i] = calculate_dp_value(min_value, hs[i], C)
    return dp[-1]

def initialize_dp(N):
    return [0] * N

def create_convex_hull_trick():
    return ConvexHullTrickWrapper()

def add_line_to_cht(cht, hs, dp, i):
    slope = calculate_slope(hs, i)
    intercept = calculate_intercept(dp, hs, i)
    cht.add_line((slope, intercept))

def calculate_slope(hs, i):
    return -2 * hs[i-1]

def calculate_intercept(dp, hs, i):
    return dp[i-1] + hs[i-1] ** 2

def query_min_value(cht, x):
    return cht.get_min(x)

def calculate_dp_value(min_value, h, C):
    return min_value + h ** 2 + C

class ConvexHullTrickWrapper:
    def __init__(self):
        self.lines = deque()
        self.count = 0

    def add_line(self, line):
        while self.has_enough_lines() and self.is_bad_line(self.lines[-2], self.lines[-1], line):
            self.remove_last_line()
        self.add_new_line(line)

    def has_enough_lines(self):
        return self.count >= 2

    def remove_last_line(self):
        self.lines.pop()
        self.count -= 1

    def add_new_line(self, line):
        self.lines.append(line)
        self.count += 1

    def is_bad_line(self, L1, L2, L3):
        return check_non_minimal(L1, L2, L3)

    def get_min(self, x):
        value = get_y(self.lines[0], x)
        while self.has_enough_lines_for_query():
            next_value = get_y(self.lines[1], x)
            if not is_better(next_value, value):
                break
            value = next_value
            self.remove_first_line()
        return value

    def has_enough_lines_for_query(self):
        return self.count >= 2

    def remove_first_line(self):
        self.lines.popleft()
        self.count -= 1

def check_non_minimal(L1, L2, L3):
    a1, b1 = L1
    a2, b2 = L2
    a3, b3 = L3
    return (a1 - a2) * (b2 - b3) >= (a2 - a3) * (b1 - b2)

def get_y(line, x):
    a, b = line
    return a * x + b

def is_better(next_value, current_value):
    return next_value <= current_value

main()