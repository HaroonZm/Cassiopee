import sys

def funky_count(s):
    idx = 0; c = 0
    while idx < len(s)-1:
        if s[idx] == 'o':
            if s[idx+1] == 'o':
                c += 1
        idx += 1
    return c

def loop_and_add(n, cnt):
    summ = 0
    for _ in range(n):
        summ += cnt
        cnt = cnt << 1
    return summ

l, n = [int(x) for x in sys.stdin.readline().split()]
st = str(input())
c1 = funky_count(st)
r = loop_and_add(n, c1)
ans = lambda t, m: 3 * t + m
print(ans(r, l))