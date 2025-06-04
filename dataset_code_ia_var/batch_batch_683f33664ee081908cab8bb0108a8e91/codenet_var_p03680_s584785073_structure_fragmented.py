def read_n():
    return int(input())

def read_next_int():
    return int(input())

def read_input_list(N):
    return [read_next_int() for _ in range(N)]

def initialize_counter():
    return 0

def initialize_l():
    return 1

def get_next_index(a, l):
    return a[l-1]

def increment_counter(cnt):
    return cnt + 1

def check_target(l):
    return l == 2

def print_result(result):
    print(result)

def print_negative_one():
    print(-1)

def main():
    N = read_n()
    a = read_input_list(N)
    cnt = initialize_counter()
    l = initialize_l()
    finished = False

    def iterate(i, cnt, l, a):
        l_next = get_next_index(a, l)
        cnt_next = increment_counter(cnt)
        if check_target(l_next):
            print_result(cnt_next)
            return True, cnt_next, l_next
        return False, cnt_next, l_next

    for i in range(N):
        done, cnt, l = iterate(i, cnt, l, a)
        if done:
            finished = True
            break
    if not finished:
        print_negative_one()

main()