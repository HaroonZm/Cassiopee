n = int(input())
s = [input() for _ in range(n)]

import collections
cnt = collections.Counter(s)
dict = sorted(cnt)

max_vote = max(cnt.values())
ans = []
for a,b in cnt.items():
  if max_vote == b:
    ans.append(a)
ans = sorted(ans)
print('\n'.join(ans))