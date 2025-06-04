n = int(input())
A = input().split()
for i in range(n):
    A[i] = int(A[i])

ans = 0

for i in range(n):
    a = A[i]
    while a % 2 == 0:
        a = a // 2
        ans = ans + 1

print(ans)