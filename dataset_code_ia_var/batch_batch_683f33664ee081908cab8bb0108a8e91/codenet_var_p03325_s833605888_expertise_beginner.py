N = int(input())
A = input().split()
ans = 0
for a in A:
    num = int(a)
    while num % 2 == 0:
        ans = ans + 1
        num = num // 2
print(ans)