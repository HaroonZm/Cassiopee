import sys
import math

N = None
for line in sys.stdin:
    for word in line.strip().split():
        N = int(word)
        break
    if N is not None:
        break

ans = 100000000000000000
amax = math.floor(math.sqrt(N))
i = 1
while i <= amax:
    if N % i == 0:
        current = i + (N // i) - 2
        if current < ans:
            ans = current
    i += 1

print(ans)