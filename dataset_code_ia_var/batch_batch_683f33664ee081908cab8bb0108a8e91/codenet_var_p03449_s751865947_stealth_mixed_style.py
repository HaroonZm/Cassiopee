N = int(input())
A = [int(x) for x in input().split()]
B = input().split()
for k in range(len(B)):
    B[k] = int(B[k])
res = 0
i = 0
while i < N:
    sm = 0
    for j in range(i+1):
        sm += A[j]
    btail = 0
    cnt = i
    while cnt < N:
        btail += B[cnt]
        cnt += 1
    if (sm + btail > res):
        res = sm + btail
    i += 1
print(res)