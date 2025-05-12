import sys
n = int(input())
m = int(input())

s = [m]
for i in range(1, n+1):
    a, b = map(int, input().split())
    m = m + a - b
    if m < 0:
        print(0)
        sys.exit(0)
    s.append(m)
print(max(s))