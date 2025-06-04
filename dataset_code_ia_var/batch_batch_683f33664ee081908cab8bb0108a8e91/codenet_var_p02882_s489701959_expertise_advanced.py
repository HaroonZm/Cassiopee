from math import degrees, acos, atan

def compute_angle(a: int, b: int, x: int) -> float:
    vol = a * a * b
    half = 0.5 * vol
    if x <= half:
        h = 2 * x / (a * b)
        hy = (h * h + b * b) ** 0.5
        # Simplify cosa using only b and h
        cosa = b / hy
        angle = 90 + degrees(acos(cosa))
    else:
        empty_height = 2 * (vol - x) / (a * a)
        angle = degrees(atan(empty_height))
    return angle

print(compute_angle(*map(int, input().split())))