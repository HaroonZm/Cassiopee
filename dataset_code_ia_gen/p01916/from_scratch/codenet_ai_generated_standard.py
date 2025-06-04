from collections import Counter
s = input().strip()
c = Counter(s)
odd = sum(v % 2 for v in c.values())
print(0 if odd <= 1 else odd - 1)