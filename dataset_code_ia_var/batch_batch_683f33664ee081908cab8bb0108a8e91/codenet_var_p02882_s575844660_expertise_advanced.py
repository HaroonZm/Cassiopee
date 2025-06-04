from math import atan, degrees

def main():
    a, b, x = map(int, input().split())
    y = x / a
    area_half = (a * b) / 2
    if y <= area_half:
        angle = 90 - degrees(atan(2 * y / b**2))
    else:
        angle = degrees(atan(2 * (a * b - y) / a**2))
    print(angle)

if __name__ == "__main__":
    main()