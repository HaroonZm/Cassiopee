H, W = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0
for i in range(H):
    for j in range(W):
        total += min(A[i], B[j])

print(total)