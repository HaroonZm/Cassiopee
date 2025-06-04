def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def is_non_increasing(a, b):
    return a <= b

def update_count(cnt):
    return cnt + 1

def reset_count():
    return 0

def update_ans(ans, cnt):
    return max(ans, cnt)

def get_max_of_two(a, b):
    return max(a, b)

def process_sequence(n, h):
    ans = 0
    cnt = 0
    for i in range(1, n):
        if is_non_increasing(h[i], h[i-1]):
            cnt = update_count(cnt)
        else:
            ans = update_ans(ans, cnt)
            cnt = reset_count()
    return get_max_of_two(ans, cnt)

def main():
    n = read_int()
    h = read_int_list()
    result = process_sequence(n, h)
    print(result)

main()