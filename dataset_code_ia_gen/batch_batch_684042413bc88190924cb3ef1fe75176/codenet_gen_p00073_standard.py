import math
while True:
    x = int(input())
    h = int(input())
    if x == 0 and h == 0:
        break
    l = math.sqrt(h**2 + (x/2)**2)
    S = x**2 + 2 * x * l
    print(f"{S:.6f}")