N = int(input())
A = [int(x) for x in input().split()]

A.sort()
ans = sum(A)
for a in A:
    if ans % 2 == 0 or a % 2 == 0:
        continue
    ans -= a

ans = ans//2
print(ans)