import sys
import math

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

g = nums[0]
for num in nums[1:]:
    g = math.gcd(g, num)

divs = []
i = 1
while i * i <= g:
    if g % i == 0:
        divs.append(i)
        if i != g // i:
            divs.append(g // i)
    i += 1

for d in sorted(divs):
    print(d)