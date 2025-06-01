N = int(input())
A = list(map(int, input().split()))
for d in range(1, N+2):
    pos = 0
    while pos < N+1:
        pos += d
        if pos <= N and A[pos-1] == 1:
            break
    else:
        print(d)
        break