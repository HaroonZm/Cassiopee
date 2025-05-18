N = int(input())
A = list(map(int, input().split()))

ex = 0

ans = 0
j = 0
ex = 0
for i in range(N):
    while j <= N-1 and ex + A[j] == ex ^ A[j]:
        ex += A[j]
        j += 1

    ans += j-i  
    ex -= A[i]

print(ans)