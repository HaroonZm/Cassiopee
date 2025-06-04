from math import isqrt

def is_sankaku(v):
    d = 8 * v + 1
    s = isqrt(d)
    return s * s == d and (s - 1) % 2 == 0

def check(lst):
    return lst == list(range(1, len(lst) + 1))

def solve():
    while True:
        if (N := int(input())) == 0:
            break
        lst = list(map(int, input().split()))
        if not is_sankaku(sum(lst)):
            print(-1)
            continue
        for count in range(10000):
            if check(lst):
                print(count)
                break
            spam = len(lst)
            lst = [x - 1 for x in lst if x > 1] + [spam]
        else:
            print(-1)

if __name__ == "__main__":
    solve()