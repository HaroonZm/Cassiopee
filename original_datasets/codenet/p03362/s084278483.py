from math import *
n = int(input())
ps = set(range(2, 55556))
for i in range(2, floor(sqrt(55555) + 1)):
    if i in ps:
        k = 2
        while(i*k <= 55555):
            if i*k in ps:
                ps.remove(i*k)
            k += 1
ans = []
i = max(ps)
while len(ans) < n and i <= 55555:
    if i in ps:
        ans.append(i)
    i -= 25
print(*ans)