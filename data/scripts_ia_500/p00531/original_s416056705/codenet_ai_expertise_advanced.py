p, a, b, c, d = (int(input()) for _ in range(5))
print(min(p*a, b + max(p - c, 0)*d))