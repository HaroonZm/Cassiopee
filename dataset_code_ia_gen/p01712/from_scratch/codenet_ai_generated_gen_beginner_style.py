N,W,H = map(int, input().split())
routers = []
for _ in range(N):
    x,y,w = map(int, input().split())
    routers.append((x,y,w))

covered_left = False
covered_right = False
covered_bottom = False
covered_top = False

for x,y,w in routers:
    if x - w <= 0:
        covered_left = True
    if x + w >= W:
        covered_right = True
    if y - w <= 0:
        covered_bottom = True
    if y + w >= H:
        covered_top = True

if covered_left and covered_right and covered_bottom and covered_top:
    print("Yes")
else:
    print("No")