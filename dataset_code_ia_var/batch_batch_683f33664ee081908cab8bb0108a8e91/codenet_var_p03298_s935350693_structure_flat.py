from collections import Counter
from itertools import product

N = int(input())
S = list(input())
S_rev = list(reversed(S[N:]))

leftlist = []
rightlist = []

for bits in product([0, 1], repeat=N):
    red_left = ''
    blue_left = ''
    red_right = ''
    blue_right = ''
    j = 0
    while j < N:
        if bits[j]:
            red_left += S[j]
            blue_right += S_rev[j]
        else:
            blue_left += S[j]
            red_right += S_rev[j]
        j += 1
    leftlist.append(red_left + "|" + blue_left)
    rightlist.append(blue_right + "|" + red_right)

left = Counter()
right = Counter()
i = 0
while i < len(leftlist):
    left[leftlist[i]] += 1
    right[rightlist[i]] += 1
    i += 1

answer = 0
for k in left:
    if k in right:
        answer += left[k] * right[k]
print(answer)