def read_input():
    return input().split()

def parse_N_T(input_list):
    return int(input_list[0]), int(input_list[1])

def read_t():
    return input().split()

def parse_t(t_strs):
    return list(map(int, t_strs))

def initial_s(T):
    return T

def initial_f(t, T):
    return t[0] + T

def compute_next_s(s, T):
    return s + T

def overlap_amount(f, next_t):
    return max(0, f - next_t)

def adjust_s_for_overlap(s, overlap):
    return s - overlap

def next_f(t_i1, T):
    return t_i1 + T

def iterate_over_times(N, t, T, s, f):
    for i in range(N-1):
        s = compute_next_s(s, T)
        overlap = 0
        if f > t[i+1]:
            overlap = overlap_amount(f, t[i+1])
        s = adjust_s_for_overlap(s, overlap)
        f = next_f(t[i+1], T)
    return s

def main():
    input_list = read_input()
    N, T = parse_N_T(input_list)
    t_strs = read_t()
    t = parse_t(t_strs)
    s = initial_s(T)
    f = initial_f(t, T)
    s = iterate_over_times(N, t, T, s, f)
    print(s)

main()