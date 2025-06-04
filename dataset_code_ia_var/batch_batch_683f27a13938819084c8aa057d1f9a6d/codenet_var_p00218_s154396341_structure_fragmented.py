def get_input():
    return int(input())

def should_stop(n):
    return n == 0

def get_scores():
    return tuple(map(int, input().split()))

def has_hundred(m, e, j):
    return m == 100 or e == 100 or j == 100

def mean2(m, e):
    return (m + e) / 2

def mean3(m, e, j):
    return (m + e + j) / 3

def is_A_hundred(m, e, j):
    return has_hundred(m, e, j)

def is_A_mean2_90(m, e):
    return mean2(m, e) >= 90

def is_A_mean3_80(m, e, j):
    return mean3(m, e, j) >= 80

def is_B_mean3_70(m, e, j):
    avg = mean3(m, e, j)
    return avg >= 70 and avg < 80

def is_B_mean3_50_and_80(m, e, j):
    avg = mean3(m, e, j)
    return avg >= 50 and avg < 70 and (m >= 80 or e >= 80)

def print_A():
    print("A")

def print_B():
    print("B")

def print_C():
    print("C")

def process_scores(m, e, j):
    if is_A_hundred(m, e, j):
        print_A()
    elif is_A_mean2_90(m, e):
        print_A()
    elif is_A_mean3_80(m, e, j):
        print_A()
    elif is_B_mean3_70(m, e, j):
        print_B()
    elif is_B_mean3_50_and_80(m, e, j):
        print_B()
    else:
        print_C()

def process_loop_iteration():
    n = get_input()
    if should_stop(n):
        return False
    for _ in range(n):
        m, e, j = get_scores()
        process_scores(m, e, j)
    return True

def main():
    while True:
        if not process_loop_iteration():
            break

main()