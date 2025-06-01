import math

def main():
    x = math.radians(90)
    px = 0
    py = 0
    while True:
        line = input()
        d_str, angle_str = line.split(",")
        d = int(d_str)
        angle = int(angle_str)
        if d == 0 and angle == 0:
            break
        px = px + math.cos(x) * d
        py = py + math.sin(x) * d
        x = x - math.radians(angle)
    print(int(px))
    print(int(py))

main()