A, B, C = map(int, input().split())

result = min(A + B + 1, C) + B

print(str(result))