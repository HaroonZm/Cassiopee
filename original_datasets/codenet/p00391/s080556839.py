W, H = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
A.sort(reverse=1)
ok =+ (sum(A) == sum(B))
for a in A:
    B.sort(reverse=1)
    for i in range(a):
        if i >= len(B) or B[i] == 0:
            ok = 0
            break
        B[i] -= 1
print(ok)