A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

max_poison_cookie = A + B + 1
if C < max_poison_cookie:
    total = C + B
else:
    total = max_poison_cookie + B
print(total)