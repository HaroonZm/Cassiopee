while 1:
    try:
        ax, ay, bx, by, cx, cy, dx, dy = map(float, input().split())
    except:
        break
    if (ax <= dx and cx <= bx) and (ay <= dy and cy <= by):
        print('YES')
    else:
        print('NO')