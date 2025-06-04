n = int(input())
t, h = 0, 0
for i in range(n):
    a, b = map(str, input().split())
    if a < b:
        h += 3
    if a == b:
        t += 1
        h += 1
    if a > b:
        t += 3
print(t, h)