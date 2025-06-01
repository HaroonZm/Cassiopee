import sys

BIG_NUM = 2000000000

def read_integer():
    return int(input())

def read_integer_list():
    return list(map(int, input().split()))

def set_recursion_limit(limit):
    sys.setrecursionlimit(limit)

def sort_descending(lst):
    lst.sort(reverse=True)

def is_termination_condition(value):
    return value == 0

def initialize_counters():
    return 0, BIG_NUM, 0

def check_win_condition(me_val, enemy_val):
    return me_val > enemy_val

def update_num_win(num_win):
    return num_win + 1

def exceeds_half(num_win, index):
    return num_win > (index + 1) // 2

def print_result(ans):
    if ans == BIG_NUM:
        print("NA")
    else:
        print("%d" % ans)

def process_single_case(N):
    me = read_integer_list()
    enemy = read_integer_list()
    sort_descending(me)
    sort_descending(enemy)
    num_win, ans, k = initialize_counters()
    for i in range(N - 1):
        if check_win_condition(me[i], enemy[k]):
            num_win = update_num_win(num_win)
            if exceeds_half(num_win, i):
                ans = i + 1
                break
        else:
            k += 1
    print_result(ans)

def main_loop():
    set_recursion_limit(100000)
    while True:
        N = read_integer()
        if is_termination_condition(N):
            break
        process_single_case(N)

main_loop()