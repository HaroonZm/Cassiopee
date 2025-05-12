import math

while True:
    b = int(input())
    if b == 0:
        break
    k_max = int(((-1 + math.sqrt(1 + 8 * b)) / 2))
    for k in range(k_max, 0, -1):
        if 2 * b % k == 0 and (2 * b / k + 1 - k) % 2 == 0:
            n = int((2 * b / k + 1 - k) / 2)
            print("{} {}".format(n, k))
            break