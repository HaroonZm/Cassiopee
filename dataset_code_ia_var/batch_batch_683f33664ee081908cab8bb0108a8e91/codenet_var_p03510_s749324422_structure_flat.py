N = int(input())
A = 0
p = 0
ans = 0
i = 0
while i < N:
    values = input().split()
    x = int(values[0])
    s = int(values[1])
    A = max(0, A - (x - p)) + s
    if A > ans:
        ans = A
    p = x
    i += 1
print(ans)