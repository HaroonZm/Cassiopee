n = int(input())
A = list(map(int, input().split()))
q = int(input())

for i in range(q):
    b, e, t = list(map(int, input().split()))
    
    for j in range(e - b):
        A[b + j], A[t + j] = A[t + j], A[b + j]

print(*A)