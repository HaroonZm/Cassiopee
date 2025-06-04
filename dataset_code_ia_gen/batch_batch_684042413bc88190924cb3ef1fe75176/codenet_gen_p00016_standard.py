import math

x = y = angle = 0.0
while True:
    line = input()
    if line == "0,0":
        break
    d, t = map(int, line.split(","))
    angle += t
    rad = math.radians(angle)
    x += d * math.cos(rad)
    y += d * math.sin(rad)

print(int(x))
print(int(y))