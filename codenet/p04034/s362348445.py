n,m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

ball = [1] * (n+1)
red = [0] * (n+1)
red[1] = 1

for x,y in xy:
    ball[x] -= 1
    ball[y] += 1
    if red[x] == 1:
        red[y] = 1
        if ball[x] == 0:
            red[x] = 0
print(sum(red))