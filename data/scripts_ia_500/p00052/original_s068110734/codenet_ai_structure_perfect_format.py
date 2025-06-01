import math
v = 0
while True:
    n = int(input())
    if n == 0:
        break
    s = 0
    for i in range(1, 7):
        s += n // (5 ** i)
    print(s)