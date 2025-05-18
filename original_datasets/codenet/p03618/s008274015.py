from collections import Counter
s = input().rstrip()
cnt = Counter(s)
total = len(s)

ans = 0
for c in s:
    cnt[c] -= 1
    total -= 1
    ans += total - cnt[c]
print(ans + 1)