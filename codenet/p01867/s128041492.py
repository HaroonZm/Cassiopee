from collections import Counter
n = int(input())
s = input()
counter = Counter(s[0::2])
counter2 = Counter(counter.values())
ans = 0
for k, v in counter2.items():
  if k == 1:
    ans += 2 * v
  else:
    if v == 1:
      ans += 4
    else:
      ans += 4 + v * 2
print(ans - 1)