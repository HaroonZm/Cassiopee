A, B, C, K = map(int, input().split())

cnt = K
if K <= A:
    cnt = K
elif K <= A+B:
    cnt = A
elif K <= A+B+C:
    cnt = A - (K-(A+B))

print(cnt)