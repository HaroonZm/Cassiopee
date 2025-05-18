N = int(input())
M = int(input())
A = list(map(int, input().split()))
S = [0 for i in range(N)]

for i in range(M) :
    B = list(map(int, input().split()))
    for j in range(N) :
        if(B[j] == A[i]) :
            S[j] += 1
        else :
            pass
    S[A[i] - 1] += N - B.count(A[i])

for i in range(N) :
    print(S[i])