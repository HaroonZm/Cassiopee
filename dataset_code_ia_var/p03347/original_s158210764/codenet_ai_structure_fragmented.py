def read_input_size():
    return int(input())

def init_list(size):
    return [0] * size

def fill_list(A, N):
    for i in range(N):
        A[i] = read_value()
    return A

def read_value():
    return int(input())

def check_first_zero(A):
    return A[0] == 0

def calculate_difference(a, b):
    return a - b

def process_d_value(d, a_i, ans):
    if d > 1:
        if a_i != 0:
            return False, ans
    elif d == 1:
        ans += 1
    else:
        ans += a_i
    return True, ans

def print_result(possible, ans):
    if possible:
        print(ans)
    else:
        print(-1)

def main():
    N = read_input_size()
    A = init_list(N)
    A = fill_list(A, N)
    possible = 1 if check_first_zero(A) else 0
    ans = 0
    if not possible:
        print_result(possible, ans)
        return
    for i in range(1, N):
        d = calculate_difference(A[i], A[i-1])
        is_possible, ans = process_d_value(d, A[i], ans)
        if not is_possible:
            possible = 0
            break
    print_result(possible, ans)

main()