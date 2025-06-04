import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
n = int(input())
a = [None]*n
i = 0
while i < n:
    a[i] = int(input())
    i += 1
ans = a[0] - 1
prev = 1
i = 1
while i < n:
    num = a[i]
    if prev + 1 < num:
        while num - (prev + 1) > 0:
            v = (num - 1)//(prev + 1)
            num -= v * (prev + 1)
            ans += v
            if num == prev + 1:
                num = prev
                break
    if prev < num:
        prev = num
    i += 1
print(ans)