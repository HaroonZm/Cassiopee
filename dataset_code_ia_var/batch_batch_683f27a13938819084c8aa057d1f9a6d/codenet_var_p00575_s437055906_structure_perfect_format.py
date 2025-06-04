A, B, C = map(int, input().split())
ans = 0
k = C // (7 * A + B)
C -= k * (7 * A + B)
if C <= 7 * A:
    print(7 * k + (C + A - 1) // A)
else:
    print(7 * (k + 1))