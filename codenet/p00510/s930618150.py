n = int(input())
m = int(input())
S_max = m
for i in range(n):
    a, b = map(int, input().split())
    m += a - b
    if m < 0:
        print(0)
        break
    S_max = max(S_max, m)
else:
    print(S_max)