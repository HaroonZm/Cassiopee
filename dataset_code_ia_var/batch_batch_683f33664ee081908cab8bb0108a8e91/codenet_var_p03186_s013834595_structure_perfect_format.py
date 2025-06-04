A, B, C = map(int, input().split())
cure = A + B - C
if cure > -1:
    print(B + C)
else:
    print(B + C + cure + 1)