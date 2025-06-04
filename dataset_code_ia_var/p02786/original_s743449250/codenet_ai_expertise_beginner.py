N = int(input())

n = 0
x = N
while x > 1:
    x = x // 2
    n = n + 1

ans = 1
i = 0
while i < n:
    ans = ans + (2 ** (i + 1))
    i = i + 1

print(ans)