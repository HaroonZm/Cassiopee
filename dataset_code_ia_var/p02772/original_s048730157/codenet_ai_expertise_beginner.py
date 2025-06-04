N = int(input())
A = input().split()
cnt = 0
for i in range(N):
    a = int(A[i])
    if a % 2 == 0:
        if a % 3 == 0:
            cnt = cnt + 1
        elif a % 5 == 0:
            cnt = cnt + 1
    else:
        cnt = cnt + 1
if cnt == N:
    print("APPROVED")
else:
    print("DENIED")