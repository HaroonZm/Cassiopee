def read_n():
    return int(input())

def read_a():
    return list(map(int, input().split()))

def less_than(val1, val2):
    return val1 < val2

def greater_than(val1, val2):
    return val1 > val2

def update_flag_from_neutral(a, i, flag):
    if less_than(a[i], a[i+1]):
        return 1
    elif greater_than(a[i], a[i+1]):
        return -1
    return flag

def handle_increasing(a, i, flag, cnt):
    if less_than(a[i], a[i+1]):
        return flag, cnt
    elif greater_than(a[i], a[i+1]):
        return 0, cnt + 1
    return flag, cnt

def handle_decreasing(a, i, flag, cnt):
    if greater_than(a[i], a[i+1]):
        return flag, cnt
    elif less_than(a[i], a[i+1]):
        return 0, cnt + 1
    return flag, cnt

def process_sequence(a, n):
    cnt = 0
    flag = 0
    i = 0
    while i < n - 1:
        if flag == 0:
            flag = update_flag_from_neutral(a, i, flag)
        elif flag == 1:
            flag, cnt = handle_increasing(a, i, flag, cnt)
        elif flag == -1:
            flag, cnt = handle_decreasing(a, i, flag, cnt)
        i += 1
    return cnt

def print_result(result):
    print(result)

def main():
    n = read_n()
    a = read_a()
    cnt = process_sequence(a, n)
    print_result(cnt + 1)

main()