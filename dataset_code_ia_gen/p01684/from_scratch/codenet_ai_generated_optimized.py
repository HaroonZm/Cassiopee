from math import pi, sqrt, acos, cos, sin

def circle_centers(U_W, U_H, A_size, B_size, AB_size):
    EPS = 1e-4
    # Impossible if AB_size > min(A_size, B_size)
    if AB_size > min(A_size, B_size):
        return None

    # Radii from areas
    rA = sqrt(A_size / pi)
    rB = sqrt(B_size / pi)

    # Rectangle constraints for centers: must fit circles with margin EPS
    min_x = rA
    max_x = U_W - rA
    min_y = rA
    max_y = U_H - rA
    # For B similarly
    min_xB = rB
    max_xB = U_W - rB
    min_yB = rB
    max_yB = U_H - rB

    # Check trivial: if AB_size = 0, place circles disjointed
    # place circle A at (rA, rA)
    # place circle B at (U_W - rB, rB) if distance > rA + rB, else adjust vertically
    if AB_size == 0:
        xA, yA = rA, rA
        xB, yB = U_W - rB, rB
        dist_sq = (xA - xB)**2 + (yA - yB)**2
        min_dist = rA + rB
        if dist_sq + EPS < min_dist ** 2:
            # try adjust yB upwards while inside rectangle
            yB_try = max_yB
            if (xA - xB)**2 + (yA - yB_try)**2 >= min_dist ** 2:
                yB = yB_try
            else:
                # try swap positions
                xA, yA = U_W - rA, rA
                xB, yB = rB, rB
                if (xA - xB)**2 + (yA - yB)**2 + EPS < min_dist ** 2:
                    return None
        return xA, yA, rA, xB, yB, rB

    # If AB_size = min(A_size,B_size) => one circle inside the other
    if AB_size == min(A_size, B_size):
        # Put circle with smaller area inside the other
        if A_size <= B_size:
            # Circle A inside B
            xA = rA
            yA = rA
            rB_eff = sqrt(B_size / pi)
            if rB_eff < rA:
                return None
            xB = rA
            yB = rA
            # Check fits inside rectangle
            if xA - rA < -EPS or xA + rA > U_W + EPS or yA - rA < -EPS or yA + rA > U_H + EPS:
                return None
            if xB - rB < -EPS or xB + rB > U_W + EPS or yB - rB < -EPS or yB + rB > U_H + EPS:
                return None
            return xA, yA, rA, xB, yB, rB
        else:
            # Circle B inside A
            xB = rB
            yB = rB
            rA_eff = sqrt(A_size / pi)
            if rA_eff < rB:
                return None
            xA = rB
            yA = rB
            if xA - rA < -EPS or xA + rA > U_W + EPS or yA - rA < -EPS or yA + rA > U_H + EPS:
                return None
            if xB - rB < -EPS or xB + rB > U_W + EPS or yB - rB < -EPS or yB + rB > U_H + EPS:
                return None
            return xA, yA, rA, xB, yB, rB

    # Otherwise, solve for distance d between centers given intersection area AB_size
    # Formula: intersection_area = rA^2 * acos((d^2 + rA^2 - rB^2)/(2 d rA)) + rB^2 * acos((d^2 + rB^2 - rA^2)/(2 d rB)) - 0.5 * sqrt((-d+rA+rB)*(d+rA-rB)*(d-rA+rB)*(d+rA+rB))

    def intersection_area(d):
        if d >= rA + rB:
            return 0.0
        if d <= abs(rA - rB):
            # one inside the other
            return pi * min(rA, rB)**2
        part1 = rA**2 * acos((d**2 + rA**2 - rB**2) / (2 * d * rA))
        part2 = rB**2 * acos((d**2 + rB**2 - rA**2) / (2 * d * rB))
        part3 = 0.5 * sqrt((-d + rA + rB) * (d + rA - rB) * (d - rA + rB) * (d + rA + rB))
        return part1 + part2 - part3

    target = AB_size
    low = abs(rA - rB)
    high = rA + rB

    # binary search distance d
    for _ in range(100):
        mid = (low + high) / 2
        val = intersection_area(mid)
        if val > target:
            low = mid
        else:
            high = mid

    d = (low + high) / 2

    # Check error
    if abs(intersection_area(d) - target) > 0.0001:
        return None

    # Place A at (rA, rA) for margin, B at (rA + d, rA)
    xA = rA
    yA = rA
    xB = xA + d
    yB = yA

    # Check if B fits inside width
    if xB + rB > U_W + 0.0001 or yB - rB < -0.0001 or yB + rB > U_H + 0.0001:
        # try move up for B until fits
        # but d fixes distance between centers, can't change horizontal distance, only vertical
        # increase yB with sqrt(rB^2 - (xB - xA)^2) to keep distance d?
        # Actually distance must remain d, so vertical offset from yA: dy = sqrt(d^2 - (xB - xA)^2)
        # But (xB - xA) is fixed by our placement (d), so no vertical offset possible because we placed on same y line
        # So try place A at (rA, rA+d) and B at (rA, rA)
        yA = rA + d
        yB = rA
        xA = rA
        xB = rA
        # Check fitting
        if ( (yA - yB)**2 + (xA - xB)**2 > (d + EPS)**2 or 
             xA - rA < -0.0001 or xA + rA > U_W + 0.0001 or yA - rA < -0.0001 or yA + rA > U_H + 0.0001 or
             xB - rB < -0.0001 or xB + rB > U_W + 0.0001 or yB - rB < -0.0001 or yB + rB > U_H + 0.0001 ):
            return None

    # Final checks inside rectangle for A and B
    if not (-0.0001 <= xA - rA and xA + rA <= U_W + 0.0001 and
            -0.0001 <= yA - rA and yA + rA <= U_H + 0.0001):
        return None
    if not (-0.0001 <= xB - rB and xB + rB <= U_W + 0.0001 and
            -0.0001 <= yB - rB and yB + rB <= U_H + 0.0001):
        return None

    return xA, yA, rA, xB, yB, rB

while True:
    line = input()
    if not line:
        break
    U_W, U_H, A_size, B_size, AB_size = map(int, line.split())
    if U_W == 0 and U_H == 0 and A_size == 0 and B_size == 0 and AB_size == 0:
        break
    res = circle_centers(U_W, U_H, A_size, B_size, AB_size)
    if res is None:
        print("impossible")
    else:
        xA, yA, rA, xB, yB, rB = res
        print(f"{xA:.9f} {yA:.9f} {rA:.9f} {xB:.9f} {yB:.9f} {rB:.9f}")