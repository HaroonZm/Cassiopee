import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

from collections import Counter
count = Counter(a)

def can(x):
    mod_count = [0,0,0]
    for k,v in count.items():
        mod_count[k%3] += v
    mod_count[0] -= (n - x)
    if mod_count[0] < 0:
        return False
    delta = mod_count[1] - mod_count[2]
    return abs(delta) <= mod_count[0]*3 and (delta - mod_count[0]*3) % 3 == 0

left, right = 1, n
res = 1
while left <= right:
    mid = (left+right)//2
    if can(mid):
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)