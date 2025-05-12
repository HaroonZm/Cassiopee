import bisect

n = int(input())
A = [int(input()) for _ in range(n)]

def LIS2(A):
    n = len(A)
    INF = max(A)+10
    L = [INF]*n
    length = 0

    for i in range(n):
        ins_ind = bisect.bisect_left(L,A[i])
        if length == ins_ind:
            length += 1
        L[ins_ind] = A[i]
    
    return length,L

L , _ = LIS2(A)
print(L)