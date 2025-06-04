n = int(input())
print(str(n)+': ', end="")
ans = []
i = 2
m = n
while i*i <= m:
    while m % i == 0:
        m //= i
        ans.append(i)
    i += 1
if m != 1:
    ans.append(m)
print(*ans)