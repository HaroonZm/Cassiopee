from string import ascii_letters
from collections import defaultdict
import sys
#input = sys.stdin.readline
def inpl(): return list(map(int, input().split()))

M = {s:i//13 for i, s in enumerate(ascii_letters)}
D = defaultdict(int)
ans = ""

input()
for s in input():
    D[M[s]] += 1

if D[0] > D[1]:
    ans = "a" * (D[0] - D[1])
else:
    ans = "z" * (D[1] - D[0])

if D[2] > D[3]:
    ans += "A" * (D[2] - D[3])
else:
    ans += "Z" * (D[3] - D[2])

print(len(ans))
print(ans)