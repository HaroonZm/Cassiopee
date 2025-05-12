from collections import Counter

n = int(input())
a = list(map(int, input().split()))

ans = 0
for key, val in Counter(a).most_common():
    if key > val:
        ans += val
    elif key < val:
        ans += val - key

print(ans)