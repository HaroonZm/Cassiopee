N = int(input())
A = list(map(int, input().split()))
del A[0]
B = list(map(int, input().split()))
del B[0]
C = list(map(int, input().split()))
del C[0]
R = [False for _ in range(N)]
for i in C:
    if A.count(i) == 0 or B.count(i) != 0:
        R[i-1] = True
print(R.count(True))