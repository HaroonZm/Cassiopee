A, B, C, D, P = (int(input()) for _ in range(5))
print(min(P * A, B + D * max(0, P - C)))