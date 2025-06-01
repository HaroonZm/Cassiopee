import math

def main():
    x = 0
    y = 0
    angle = math.radians(90)

    while True:
        line = input()
        a_str, b_str = line.split(",")
        a = float(a_str)
        b = float(b_str)
        if a == 0 and b == 0:
            break
        b = math.radians(b)

        x = x + a * math.sin(angle)
        y = y + a * math.cos(angle)
        angle = angle - b

    print(int(y))
    print(int(x))

main()