def get_n():
    return int(input())

def get_l():
    return list(map(int, input().split()))

def check_small_n(n):
    return n <= 2

def print_and_quit():
    print(1)
    quit()

def get_diff(a, b):
    return b - a

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def should_change_direction(diff, h):
    return diff * h < 0

def update_h(diff):
    if diff < 0:
        return -1
    elif diff > 0:
        return 1
    else:
        return 0

def process(l, n):
    h = 0
    ans = 1
    i = 0
    while i < n - 1:
        diff = get_diff(l[i], l[i+1])
        if should_change_direction(diff, h):
            ans += 1
            h = 0
            i += 1
            continue
        h = update_h(diff)
        i += 1
    return ans

def main():
    n = get_n()
    l = get_l()
    if check_small_n(n):
        print_and_quit()
    result = process(l, n)
    print(result)

main()