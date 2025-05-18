from collections import Counter
counter = Counter()
n, f = map(int, input().split())
for _ in range(n):
  items = input().split()
  m = int(items[0])
  items = items[1:]
  items.sort()
  for i in range(m):
    for j in range(i + 1, m):
      counter[(items[i], items[j])] += 1

lst = [(k, v) for k, v in counter.most_common() if v >= f]
lst.sort()
print(len(lst))
for k, v in lst:
  print(*k)