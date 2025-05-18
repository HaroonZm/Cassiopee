w, h, n = map(int, input().split())
xl, xr = 0, w
yd, yu = 0, h
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        if x < xl:
            continue
        elif xl <= x <= xr:
            xl = x
        else:
            xl, xr = 0, 0 # 抜けてた...
    elif a == 2:
        if xr < x:
            continue
        elif xl <= x <= xr:
            xr = x
        else:
            xl, xr = 0, 0
    elif a == 3:
        if y < yd:
            continue
        elif yd <= y <= yu:
            yd = y
        else:
            yd, yu = 0, 0
    elif a == 4:
        if y > yu:
            continue
        elif yd <= y <= yu:
            yu = y
        else:
            yd, yu = 0, 0

print((xr - xl) * (yu - yd))