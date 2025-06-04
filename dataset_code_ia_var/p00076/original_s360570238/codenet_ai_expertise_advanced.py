from math import pi, cos, sin, atan2

def compute_final_position(n: int) -> tuple[float, float]:
    ang, x, y = 0.0, 1.0, 0.0
    for _ in range(n-1):
        ang += pi/2
        x, y = x + cos(ang), y + sin(ang)
        ang = atan2(y, x)
    return round(x, 2), round(y, 2)

def main():
    while True:
        if (val := input()) == '-1':
            break
        n = int(val)
        x, y = compute_final_position(n)
        print(f"{x:.2f}\n{y:.2f}")

if __name__ == "__main__":
    main()