input()
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

B = input().split()
for i in range(len(B)):
    B[i] = int(B[i])

ans = 0

A.sort(reverse=True)

for a in A:
    B.sort(reverse=True)
    for i in range(a):
        B[i] = B[i] - 1
    ok = True
    for b in B:
        if b < 0:
            ok = False
    if not ok:
        ans = 0
        break

max_b = B[0]
if max_b == 0:
    ans = 1

print(ans)