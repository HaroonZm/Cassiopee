def read_input():
    return input()

def convert_to_list(s):
    return list(map(int, s))

def get_initial_values(n):
    return n[0], 0

def increment_counter(cnt):
    return cnt + 1

def reset_counter():
    return 0

def set_f(n, i):
    return n[i]

def should_break(cnt):
    return cnt == 3

def equals(a, b):
    return a == b

def process_loop(n, f, cnt):
    i = 0
    while i < 4:
        if should_break(cnt):
            break
        if equals(f, n[i]):
            cnt = increment_counter(cnt)
            f = set_f(n, i)
        else:
            cnt = reset_counter()
            f = set_f(n, i)
        i += 1
    return f, cnt, i-1 if i>0 else 0

def post_loop(f, n, i, cnt):
    if equals(f, n[i]):
        cnt = increment_counter(cnt)
    return cnt

def check_cnt_and_print(cnt):
    if cnt >= 3:
        print("Yes")
    else:
        print("No")

def main():
    s = read_input()
    n = convert_to_list(s)
    f, cnt = get_initial_values(n)
    f, cnt, i = process_loop(n, f, cnt)
    cnt = post_loop(f, n, i, cnt)
    check_cnt_and_print(cnt)

main()