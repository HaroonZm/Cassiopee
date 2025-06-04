def main():
    N = get_initial_input()
    while loop_condition(N):
        l = get_initial_l()
        N = decrement_N(N)
        l, N = find_l(N, l)
        s, N = compute_s(N, l)
        t, ans = get_initial_t_ans(s)
        t, l, ans, N = assign_t_l_ans(N, l, s, t, ans)
        ans = finalize_ans(ans, t)
        output_str = generate_output(ans, s, t, N, l)
        print(output_str)
        N = get_next_input()

def get_initial_input():
    return int(input())

def loop_condition(N):
    return bool(N)

def get_initial_l():
    return 2

def decrement_N(N):
    return N - 1

def calculate_threshold(l):
    return ((1 << (l - 1)) - 1) * 81

def update_N_l(N, l):
    N -= calculate_threshold(l)
    l += 1
    return N, l

def find_l(N, l):
    while N >= calculate_threshold(l):
        N, l = update_N_l(N, l)
    return l, N

def calc_denominator(l):
    return ((1 << (l - 1)) - 1) * 9

def compute_s(N, l):
    denominator = calc_denominator(l)
    s = N // denominator + 1
    N = N % denominator
    return s, N

def get_initial_t_ans(s):
    t = -1
    ans = str(s)
    return t, ans

def threshold1(l):
    return 1 << (l - 2)

def outer_loop(N, l, s, t):
    for i in range(s):
        if N >= threshold1(l):
            N -= threshold1(l)
        else:
            t = i
            break
    return N, t

def threshold2(l):
    return ((1 << (l - 2)) - 1) * 9

def inner_loop(N, l, s, t):
    for i in range(s + 1, 10):
        if N >= threshold1(l):
            N -= threshold1(l)
        else:
            t = i
            break
    return N, t

def assign_t_l_ans(N, l, s, t, ans):
    while t < 0:
        N, t = outer_loop(N, l, s, t)
        if t >= 0:
            continue
        if N >= threshold2(l):
            N -= threshold2(l)
            N, t = inner_loop(N, l, s, t)
        else:
            l -= 1
            ans += str(s)
    return t, l, ans, N

def finalize_ans(ans, t):
    ans += str(t)
    return ans

def get_binary(N):
    return bin(N)[2:]

def build_ans_(s, t, N, l):
    if s > t:
        b = get_binary(N)
        pad_char = str(t)
        rep = l - 1 - len(b)
        ans_ = pad_char * rep
        C = [str(t), str(s)]
    else:
        b = get_binary(N)
        pad_char = str(s)
        rep = l - 1 - len(b)
        ans_ = pad_char * rep
        C = [str(s), str(t)]
    for i in range(len(b)):
        ans_ += C[int(b[i])]
    return ans_

def generate_output(ans, s, t, N, l):
    ans_ = build_ans_(s, t, N, l)
    return ans + ans_[1:]

def get_next_input():
    return int(input())

main()