H1, M1, H2, M2, K = map(int, input().split())
time = (H2 - H1) * 60 + (M2 - M1)
result = time - K
print(result)