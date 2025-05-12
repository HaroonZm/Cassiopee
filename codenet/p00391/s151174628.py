input()
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
ans = 0

A.sort(reverse=True)

for a in A:
    B.sort(reverse=True)
    for i in range(a):
        B[i] -= 1
    if min(B) < 0:
        ans = 0
        break

if max(B) == 0:
    ans = 1

print(ans)