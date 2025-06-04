import sys
from string import ascii_lowercase

S = sys.stdin.readline().rstrip()
ans = float('inf')

for c in ascii_lowercase:
    if c not in S:
        continue
    seq = S
    cnt = 0
    while len(set(seq)) > 1:
        seq = ''.join(
            c if (seq[i] == c or seq[i+1] == c) else seq[i]
            for i in range(len(seq)-1)
        )
        cnt += 1
    ans = min(ans, cnt)
print(ans)