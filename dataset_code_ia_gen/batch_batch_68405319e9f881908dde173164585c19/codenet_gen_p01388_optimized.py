from collections import Counter

s = input().upper()
c = Counter(s)
print(min(c[ch] for ch in "KUPC"))