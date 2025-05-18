W, H, x, y = map(int, input().split())

area = W * H / 2
count = int(x+x == W and y+y == H)
print(area, count)