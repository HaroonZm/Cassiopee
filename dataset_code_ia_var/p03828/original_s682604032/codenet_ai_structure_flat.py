import sys
input = sys.stdin.readline
n = int(input())
INF = 10 ** 9 + 7
Num = [0] * (n + 1)
x = 2
while x <= n:
    y = x
    i = 2
    while i * 2 <= y:
        while y % i == 0:
            y = y // i
            Num[i] += 1
        i = i + 1
    if y != 1:
        Num[y] += 1
    x += 1
ans = 1
i = 0
while i < len(Num):
    ans = (ans * (Num[i] + 1)) % INF
    i += 1
print(ans)