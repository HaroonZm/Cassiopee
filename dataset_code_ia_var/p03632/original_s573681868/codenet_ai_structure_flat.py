A, B, C, D = map(int, input().split())
x = min(B, D) - max(A, C)
if x > 0:
    print(x)
if x <= 0:
    print("0")