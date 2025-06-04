while True:
    try:
        point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, point4_x, point4_y = map(float, input().split())
    except Exception:
        break
    vector1_dx = point2_x - point1_x
    vector1_dy = point2_y - point1_y
    vector2_dx = point4_x - point3_x
    vector2_dy = point4_y - point3_y
    dot_product = vector1_dx * vector2_dx + vector1_dy * vector2_dy
    epsilon_threshold = 1e-10
    if abs(dot_product) < epsilon_threshold:
        print("YES")
    else:
        print("NO")