def read_int():
    return int(input())

def read_strs():
    return input().split()

def str_to_int_list(str_list):
    return [int(num) for num in str_list]

def collect_info(N):
    info = []
    for _ in range(N):
        infocstr = read_strs()
        infoc = str_to_int_list(infocstr)
        info.append(infoc)
    return info

def calc_time(prev_t, curr_t):
    return curr_t - prev_t

def calc_need(prev_x, prev_y, curr_x, curr_y):
    return abs(prev_x - curr_x) + abs(prev_y - curr_y)

def calc_d(time, need):
    return time - need

def check_valid_move(d):
    if d < 0 or d % 2 == 1:
        return False
    return True

def update_state(infoi):
    return infoi[0], infoi[1], infoi[2]

def process_moves(info):
    t, x, y = 0, 0, 0
    for infoi in info:
        time = calc_time(t, infoi[0])
        need = calc_need(x, y, infoi[1], infoi[2])
        d = calc_d(time, need)
        if not check_valid_move(d):
            print('No')
            return
        t, x, y = update_state(infoi)
    print('Yes')

def main():
    N = read_int()
    info = collect_info(N)
    process_moves(info)

main()