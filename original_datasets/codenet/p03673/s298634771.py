n = int(input())
a = [int(x) for x in input().split()]

even = []
odd = []

for i in range(n):
    if i % 2 == 0:
        odd.append(a[i])
    else:
        even.append(a[i])

if n % 2 == 0:
    even.reverse()
    ans = even + odd
    print(*ans)
else:
    odd.reverse()
    ans = odd + even
    print(*ans)