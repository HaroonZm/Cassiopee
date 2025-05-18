n = int(input())
A = list(map(int, input().split()))
l = 1
r = 2*n
while l < r-1:
    mid = (l+r)//2
    B = []
    C = []
    for i in range(0,2*n-1):
        B.append(A[i] >= mid)
        C.append(0)
    for i in range(1,2*n-1):
        if B[i-1] == B[i]:
            C[i] = 1
    for i in range(0,2*n-2):
        if B[i+1] == B[i]:
            C[i] = 1
    mi = 2*n
    ans = False
    for i in range(0,2*n-1):
        if C[i] == 1:
            if abs(i-n+1) < mi:
                mi = abs(i-n+1)
                ans = B[i]
    if mi == 2*n:   #specialfall
        ans = ((n+1)%2)^B[n-1]
    if ans == True:
        l = mid
    else:
        r = mid
print(l)