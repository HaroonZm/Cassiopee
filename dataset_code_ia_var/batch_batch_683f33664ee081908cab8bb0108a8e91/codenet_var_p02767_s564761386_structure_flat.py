N = int(input())
A = [int(x) for x in input().rstrip().split()]
ave = sum(A) // len(A)
ans = 0
if N / 2 < (sum(A) % len(A)):
    ave += 1
i = 0
while i < len(A):
    ans += (A[i] - ave) ** 2
    i += 1
print(ans)