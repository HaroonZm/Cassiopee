import math

n = int(input())
lis = []
cou = 0
ans = 0

for i in range(n):
    a = int(input())
    cou = max(cou, a)
    lis.append(a)

num = []
for i in range(1, cou + 1):
    if cou % i == 0:
        num.append(i)

for nu in lis:
    co = 0
    while num[co] < nu:
        co += 1
    ans += (num[co] - nu)

print(ans)