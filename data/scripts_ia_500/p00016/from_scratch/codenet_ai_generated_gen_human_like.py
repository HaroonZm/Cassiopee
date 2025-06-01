import math

x, y = 0.0, 0.0
angle = 0.0  # initial direction facing east (0 degrees)

while True:
    line = input().strip()
    if line == "0,0":
        break
    d_str, t_str = line.split(',')
    d = int(d_str)
    t = int(t_str)

    # Move d steps in current direction
    rad = math.radians(angle)
    x += d * math.cos(rad)
    y += d * math.sin(rad)

    # Turn clockwise by t degrees (subtract because y-axis is north)
    angle -= t

print(int(x))
print(int(y))