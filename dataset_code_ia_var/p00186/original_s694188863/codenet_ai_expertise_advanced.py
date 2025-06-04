from sys import stdin

def check(mid, b, c1, c2, q1):
    return mid + (b - mid * c1) // c2 >= q1

for line in map(str.strip, stdin):
    if line == "0":
        break
    q1, b, c1, c2, q2 = map(int, line.split())
    max_aizu = min(b // c1, q2)

    if max_aizu <= 0:
        print("NA")
        continue

    if c2 >= c1:
        max_normal = (b - max_aizu * c1) // c2
        print((f"{max_aizu} {max_normal}") if max_aizu + max_normal >= q1 else "NA")
        continue

    if (b - c1) // c2 + 1 < q1:
        print("NA")
        continue

    left, right = 0, max_aizu + 1
    while (diff := right - left) > 1:
        mid = (left + right) >> 1
        (left, right)[not check(mid, b, c1, c2, q1)] = mid

    print(left, (b - left * c1) // c2)