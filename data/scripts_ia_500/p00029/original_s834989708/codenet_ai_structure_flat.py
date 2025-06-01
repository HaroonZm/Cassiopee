from collections import Counter
l = input().split()
c = Counter()
for x in l:
    c[x] += 1
most_common = None
max_count = 0
for k, v in c.items():
    if v > max_count:
        most_common = k
        max_count = v
longest = l[0]
for x in l:
    if len(x) > len(longest):
        longest = x
print(most_common, longest)