n = int(input())
A = sorted(list(map(int, input().split())))

from itertools import accumulate

ans = 1
cumsum = list(reversed(list(accumulate(A))))

for a,cs in zip(reversed(A), cumsum[1:]):
    if a <= 2*cs:
        ans += 1
    else:
        break
print(ans)