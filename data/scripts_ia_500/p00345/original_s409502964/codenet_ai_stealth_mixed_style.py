#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    return list(sys.stdin.readline().rstrip('\n'))

def IR(n):
    res = []
    for _ in range(n):
        res.append(I())
    return res

def LIR(n):
    res = []
    for _ in range(n):
        res.append(LI())
    return res

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(10**6)
mod = 10**9 + 7

# A
def A():
    e = LI()
    d = defaultdict(int)
    for x in e:
        d[x] += 1
    for count in d.values():
        if count != 2:
            print("no")
            break
    else:
        print("yes")

# B
def B():
    n = I()
    a = LI()
    a.sort()
    ans = -math.inf
    for c in range(n):
        for d in range(c):
            diff = a[c] - a[d]
            e = None
            for i in reversed(range(n)):
                if i != c and i != d:
                    e = i
                    break
            b_idx = None
            for i in reversed(range(e)):
                if i != c and i != d:
                    b_idx = i
                    break
            if e is not None and b_idx is not None:
                val = (a[e] + a[b_idx]) / diff
                if val > ans:
                    ans = val
    print(ans)

# C
def C():
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    s = input().strip()
    if '(' not in s:
        decimal_places = len(s) - s.find('.') - 1 if '.' in s else 0
        if decimal_places == 0:
            # integer number
            print(f"{int(float(s))}/1")
            return
        numerator = int(round(float(s) * 10**decimal_places))
        denominator = 10**decimal_places
        g = gcd(numerator, denominator)
        numerator //= g
        denominator //= g
    else:
        point_index = s.find('.')
        start_repeat = s.find('(')
        non_repeat_len = start_repeat - point_index -1
        non_repeat_part = s[:start_repeat]
        non_repeat_num = float(non_repeat_part)
        numerator1 = int(round(non_repeat_num * 10**non_repeat_len)) if non_repeat_len > 0 else 0
        denominator1 = 10**non_repeat_len if non_repeat_len > 0 else 1
        repeat_part = s[start_repeat+1:-1]
        repeat_num = int(repeat_part)
        repeat_len = len(repeat_part)
        numerator2 = repeat_num
        denominator2 = (10**repeat_len - 1) * (10**non_repeat_len)
        numerator = numerator1 * denominator2 + numerator2 * denominator1
        denominator = denominator1 * denominator2
        g = gcd(numerator, denominator)
        numerator //= g
        denominator //= g
    print(f"{numerator}/{denominator}")

# D
def D():
    pass

# E
def E():
    pass

# F
def F():
    pass

# G
def G():
    pass

# H
def H():
    pass

# I
def I_():
    pass

# J
def J():
    pass

if __name__ == "__main__":
    C()