import math

def read_ints():
    return list(map(int, input().split()))

def read_n_inputs(n):
    return [int(input()) for _ in range(n)]

def compute_initial_print(h0, t):
    return math.ceil((t + 0.5) / h0)

def initialize_lists(n):
    t_first = [0] * (n + 1)
    w = [0] * n
    return t_first, w

def process_greater_than_t(t_first, i, h):
    print(1)
    return t_first[i] + h[i]

def compute_w_prev(h, w, i):
    return (h[i - 1] + w[i - 1]) - h[i]

def update_t_first(current, value):
    return current + value

def delta_t(t, t_first_i):
    return t - t_first_i

def calc_temp(delta, h_w_sum):
    return math.ceil((delta + 0.5) / h_w_sum)

def print_greater_than_prev(delta, h, w, i):
    h_w_sum = h[i] + w[i]
    temp = calc_temp(delta, h_w_sum)
    if delta % h_w_sum >= h[i]:
        print(temp + 1)
    else:
        print(temp)

def print_else_case(delta, h_i):
    print(math.ceil((delta + 0.5) / h_i))

def process_case(i, t, t_first, h, w):
    if t_first[i] > t:
        t_first[i + 1] = process_greater_than_t(t_first, i, h)
        return

    if h[i - 1] + w[i - 1] > h[i]:
        w[i] = compute_w_prev(h, w, i)
        t_first[i + 1] = update_t_first(t_first[i], h[i])
        curr_delta_t = delta_t(t, t_first[i])
        print_greater_than_prev(curr_delta_t, h, w, i)
    else:
        w[i] = 0
        t_first[i + 1] = update_t_first(t_first[i], h[i])
        curr_delta_t = delta_t(t, t_first[i])
        print_else_case(curr_delta_t, h[i])

def main():
    n, t = read_ints()
    h = [0] * n
    for i, value in enumerate(read_n_inputs(n)):
        h[i] = value

    t_first, w = initialize_lists(n)

    print(compute_initial_print(h[0], t))
    t_first[1] = h[0]

    for i in range(1, n):
        process_case(i, t, t_first, h, w)

main()