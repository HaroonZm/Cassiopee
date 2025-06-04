def read_n():
    return int(input())

def read_a():
    return list(map(int, input().split()))

def is_trivial_case(n):
    return n < 3

def print_trivial_result():
    print(1)

def exit_program():
    import sys
    sys.exit(0)

def first_difference(a):
    return a[1] - a[0]

def update_increase_on_sign_change(increase, new_inc, cnt):
    if increase * new_inc < 0:
        cnt += 1
        increase = 0
    elif increase == 0:
        increase = new_inc
    return increase, cnt

def process_differences(a):
    cnt = 1
    increase = first_difference(a)
    for i in range(2, len(a)):
        new_inc = a[i] - a[i-1]
        increase, cnt = update_increase_on_sign_change(increase, new_inc, cnt)
    return cnt

def print_result(cnt):
    print(cnt)

def main():
    n = read_n()
    a = read_a()
    if is_trivial_case(n):
        print_trivial_result()
        exit_program()
    cnt = process_differences(a)
    print_result(cnt)

main()