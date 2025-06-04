N = int(input())
w = 0
h = 1
while h < 3501:
    n = h
    while n < 3501:
        if 4 * h * n > N * (h + n) and (N * h * n) % (4 * h * n - N * (h + n)) == 0:
            w = N * h * n // (4 * h * n - N * (h + n))
            break
        n += 1
    if w > 0:
        break
    h += 1
print(h, n, w)