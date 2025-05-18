M, N = map(int,input().split())
A = list(map(int,input().split()))
if M >= 3:
    now = A[0]
    ans = 0
    for k in range(1,N):
        if A[k] == now:
            now = -1
            ans += 1
        else:
            now = A[k]
    print(ans)
else:
    now = A[0]
    ans1 = 0
    for k in range(1,N):
        if A[k] == now:
            now = 3-now
            ans1 += 1
        else:
            now = A[k]

    ans2 = 1
    now = 3-A[0]
    for k in range(1,N):
        if A[k] == now:
            now = 3-now
            ans2 += 1
        else:
            now = A[k]

    print(min(ans1,ans2))