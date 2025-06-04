n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

def lis_simple(A):
    n = len(A)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
    max_lis = 0
    for x in dp:
        if x > max_lis:
            max_lis = x
    return max_lis

print(lis_simple(A))