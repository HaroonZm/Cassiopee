n = int(input())
p = [int(a) for a in input().split()]
cnt = 0

i = 0
while i < n - 2:
    x = p[i]
    y = p[i+1]
    z = p[i+2]
    if (y > x and y < z) or (y < x and y > z):
        cnt += 1
    i += 1

print(cnt)