while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    black = [tuple(map(int, input().split())) for _ in range(n)]
    white = [tuple(map(int, input().split())) for _ in range(m)]
    points = black + white

    def side(p1, p2, p):
        return (p2[0]-p1[0])*(p[1]-p1[1]) - (p2[1]-p1[1])*(p[0]-p1[0])

    def can_separate():
        # Try all pairs of points to define a candidate line
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                on_positive = []
                on_negative = []
                on_line = False
                for k in range(len(points)):
                    if k == i or k == j:
                        continue
                    val = side(p1, p2, points[k])
                    if val == 0:
                        on_line = True
                        break
                    elif val > 0:
                        on_positive.append(k)
                    else:
                        on_negative.append(k)
                if on_line:
                    continue
                # Check if one side has only black and other only white
                def all_black(indices):
                    for idx in indices:
                        if idx >= n:
                            return False
                    return True
                def all_white(indices):
                    for idx in indices:
                        if idx < n:
                            return False
                    return True

                if (all_black(on_positive) and all_white(on_negative)) or (all_white(on_positive) and all_black(on_negative)):
                    return True
        return False

    if can_separate():
        print("YES")
    else:
        print("NO")