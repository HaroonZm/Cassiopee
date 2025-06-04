def read_input():
    return input()

def parse_int_list(s):
    return [int(item) for item in s.split()]

def get_N_T():
    line = read_input()
    return parse_int_list(line)

def get_t_list():
    line = read_input()
    return parse_int_list(line)

def initial_time(T):
    return T

def delta_time(current, previous):
    return current - previous

def min_time(T, dt):
    return min(T, dt)

def update_time(time, increment):
    return time + increment

def process_times(N, T, t_list):
    time = 0
    for i in range(N):
        if is_first_index(i):
            time = initial_time(T)
        else:
            dt = delta_time(t_list[i], t_list[i-1])
            add_time = min_time(T, dt)
            time = update_time(time, add_time)
    return time

def is_first_index(i):
    return i == 0

def print_result(time):
    print(time)

def resolve():
    N_T = get_N_T()
    N, T = N_T[0], N_T[1]
    t_list = get_t_list()
    total_time = process_times(N, T, t_list)
    print_result(total_time)

if __name__ == "__main__":
    resolve()