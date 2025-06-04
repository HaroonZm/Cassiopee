s = input()
N = len(s)
_inf = N + 1
nxt = []
for _ in range(N+1):
    row = []
    idx = 0
    while idx < 26:
        row.append(_inf)
        idx += 1
    nxt.append(row)

for idx, char in list(enumerate(reversed(s))):
    cix = ord(char) - ord("a")
    for alph in range(26):
        if alph == cix:
            nxt[N-idx-1][alph] = N-idx-1
        else:
            nxt[N-idx-1][alph] = nxt[N-idx][alph]

dp = [_inf]*N + [N] * 3
dp[_inf] = 0
dp[_inf+1] = 0

def min_in_row(row, table):
    minv = _inf + 1
    for alph in range(26):
        t = table[row[alph] + 1] + 1
        if t < minv: minv = t
        if minv == 1: return minv
    return minv

i = N
while i >= 0:
    t = min_in_row(nxt[i], dp)
    dp[i] = t
    i -= 1

from collections import deque
q = deque()
cur = 0
v = dp[0] - 1
import itertools

while v >= 0:
    for k in itertools.chain(range(26)):
        if dp[nxt[cur][k]+1] == v:
            q.append(chr(k+97))
            cur = nxt[cur][k] + 1
            break
    v -= 1

print("".join(list(q)))