EPS = 1e-7

while True:
    d = float(input())
    if d == 0:
        break
    px, py, vx, vy = map(float, input().split())
    
    dp = (px ** 2 + py ** 2) ** 0.5
    dv = (vx ** 2 + vy ** 2) ** 0.5
    
    # Dot product normalized
    if dp != 0 and dv != 0:
        x = (px * vx + py * vy) / (dp * dv)
    else:
        x = 0.0  # Avoid division by zero
    
    ans = d + 1
    
    if abs(x + 1) <= EPS:
        ans = dp
    elif abs(1 - x) <= EPS:
        ans = 2 - dp
    
    if abs(ans - d) <= EPS or ans <= d:
        print(ans)
    else:
        print("impossible")