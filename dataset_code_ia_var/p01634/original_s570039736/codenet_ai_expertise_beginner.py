A = 0
n = input()
if len(n) >= 6:
    A = A + 1
B = 0
for c in n:
    if c in "0123456789":
        B = B + 1
if B > 0:
    A = A + 1
C = 0
for c in n:
    if c in "abcdefghijklmnopqrstuvwxyz":
        C = C + 1
if C > 0:
    A = A + 1
D = 0
for c in n:
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        D = D + 1
if D > 0:
    A = A + 1
if A == 4:
    print('VALID')
else:
    print('INVALID')