A, B, C, D, P = map(int, (input() for _ in range(5)))
print(min(A * P, B + max(0, P - C) * D))