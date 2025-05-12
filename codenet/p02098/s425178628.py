a, b = int(input()), int(input())
print((a + b) / 2 % 360 if abs (a - b) % 360 < 180 else (a + b + 360) / 2 % 360)