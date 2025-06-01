W, H = input().split()
W = int(W)
H = int(H)

A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

B = input().split()
for i in range(len(B)):
    B[i] = int(B[i])

A.sort(reverse=True)

if sum(A) == sum(B):
    ok = 1
else:
    ok = 0

for a in A:
    B.sort(reverse=True)
    for i in range(a):
        if i >= len(B) or B[i] == 0:
            ok = 0
            break
        else:
            B[i] = B[i] - 1
    if ok == 0:
        break

print(ok)