H, N = map(int,input().split())
A = list(map(int,input().split()))

K = sum(A)

if K >= H:
    print("Yes")
else:
    print("No")