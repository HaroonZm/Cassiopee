def read_input_n():
    return int(input())

def initialize_ans():
    return 1

def initialize_h():
    return [0] * 126

def process_v(n, h):
    ans = 1
    for _ in range(n):
        v = read_single_value()
        update_h_and_ans(v, h)
        ans = increment_ans(ans, v)
    return ans

def read_single_value():
    return int(input())

def update_h_and_ans(v, h):
    if v <= 125:
        h[v] += 1

def increment_ans(ans, v):
    return ans + v

def calculate_s(h, upto):
    s = 0
    for i in range(1, upto):
        s = increment_s(s, h, i)
    return s

def increment_s(s, h, i):
    return s + h[i-1]

def should_update_ans(n, s, i):
    return n > s + 4 * i

def update_ans(ans, n, s, i):
    return ans - (n - (s + 4 * i))

def process_subtraction(ans, n, h):
    s = 0
    for i in range(1, 126):
        s = increment_s(s, h, i)
        if should_update_ans(n, s, i):
            ans = update_ans(ans, n, s, i)
    return ans

def main():
    n = read_input_n()
    h = initialize_h()
    ans = initialize_ans()
    for _ in range(n):
        v = read_single_value()
        update_h_and_ans(v, h)
        ans = increment_ans(ans, v)
    ans = process_subtraction(ans, n, h)
    print(ans)

main()