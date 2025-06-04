a = int(input())
b = int(input())
d = (b - a) % 360
if d > 180:
    d -= 360
m = (a + d/2) % 360
print(round(m, 4))