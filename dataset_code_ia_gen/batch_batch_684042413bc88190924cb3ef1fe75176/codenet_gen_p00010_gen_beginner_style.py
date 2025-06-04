n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    
    # Calculate the midpoints of two sides
    mid_x1 = (x1 + x2) / 2.0
    mid_y1 = (y1 + y2) / 2.0
    mid_x2 = (x2 + x3) / 2.0
    mid_y2 = (y2 + y3) / 2.0
    
    # Calculate the slopes of the two sides
    if x2 != x1:
        m1 = (y2 - y1) / (x2 - x1)
    else:
        m1 = None  # vertical line
    
    if x3 != x2:
        m2 = (y3 - y2) / (x3 - x2)
    else:
        m2 = None  # vertical line
    
    # Calculate the slopes of the perpendicular bisectors
    if m1 == 0:
        pm1 = None
    elif m1 is None:
        pm1 = 0
    else:
        pm1 = -1 / m1
    
    if m2 == 0:
        pm2 = None
    elif m2 is None:
        pm2 = 0
    else:
        pm2 = -1 / m2
    
    # Find intersection of the two perpendicular bisectors (circumcenter)
    if pm1 is None:
        cx = mid_x1
        if pm2 is None:
            # Both bisectors vertical, no unique solution (degenerate triangle)
            cy = mid_y2
        else:
            # Use second bisector line equation y = pm2*(x - mid_x2) + mid_y2
            cy = pm2 * (cx - mid_x2) + mid_y2
    elif pm2 is None:
        cx = mid_x2
        cy = pm1 * (cx - mid_x1) + mid_y1
    else:
        # Solve pm1*(x - mid_x1) + mid_y1 = pm2*(x - mid_x2) + mid_y2
        # pm1*x - pm1*mid_x1 + mid_y1 = pm2*x - pm2*mid_x2 + mid_y2
        # x*(pm1 - pm2) = mid_y2 - mid_y1 + pm1*mid_x1 - pm2*mid_x2
        denominator = pm1 - pm2
        if denominator == 0:
            # Lines are parallel, no unique circumcenter, use some fallback
            cx = mid_x1
            cy = mid_y1
        else:
            cx = (mid_y2 - mid_y1 + pm1 * mid_x1 - pm2 * mid_x2) / denominator
            cy = pm1 * (cx - mid_x1) + mid_y1
    
    # radius is distance from center to any vertex
    r = ((cx - x1)**2 + (cy - y1)**2) ** 0.5
    
    print(f"{cx:.3f} {cy:.3f} {r:.3f}")