from bisect import bisect_left as bl
from itertools import accumulate

h, w= map(int, input().split())
aList = sorted(map(int, input().split()))
bList = list(map(int, input().split()))
acc = [0]+list(accumulate(aList))
aList.insert(0, -1)

ans = 0
for b in bList:
    index = bl(aList, b)
    ans += acc[index - 1] + (h - index + 1) * b
print(ans)