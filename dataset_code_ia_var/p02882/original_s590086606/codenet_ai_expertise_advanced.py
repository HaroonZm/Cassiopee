from math import atan, degrees

def calculate_angle(a: int, b: int, x: int) -> float:
    base_area = a * a
    half_volume = (base_area * b) / 2
    if x >= half_volume:
        h = x / base_area
        return degrees(atan((2 * h - b) / a))
    else:
        d = (2 * x) / (b * a)
        return degrees(atan(b / d))

if __name__ == "__main__":
    a, b, x = map(int, input().split())
    print(calculate_angle(a, b, x))