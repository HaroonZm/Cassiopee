import sys
from collections import deque

mod = 10**9+7

def ns():
    return sys.stdin.readline().rstrip()

def ni():
    return int(ns())

def na():
    return list(map(int, sys.stdin.readline().split()))

def build_c_dict(n):
    c = {}
    for i in range(n//2 + 1):
        key = abs((n-1-i)-i)
        c[key] = 0
    return c

def validate_and_count(a_list, c):
    for a in a_list:
        if not a in c:
            return False
        if c[a]==2:
            return False
        c[a] += 1
    return True

def calculate_result(c):
    cnt = 1
    for k, v in c.items():
        if v == 2 or k == 0:
            cnt = (cnt * v) % mod
        else:
            return 0
    return cnt

def print_and_exit_zero():
    print(0)
    exit(0)

def main():
    n = ni()
    a_list = na()
    c = build_c_dict(n)
    if not validate_and_count(a_list, c):
        print_and_exit_zero()
    cnt = calculate_result(c)
    if not cnt:
        print_and_exit_zero()
    print(cnt)

main()