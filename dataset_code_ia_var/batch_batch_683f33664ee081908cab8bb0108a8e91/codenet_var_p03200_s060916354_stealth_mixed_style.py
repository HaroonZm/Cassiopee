S = input()
def step(s, l_s):
    res = 0
    blacks = 0
    idx = l_s - 1
    while idx > 0:
        if s[idx] == 'B':
            blacks = blacks + 1
            idx -= 1
            continue
        else:
            if s[idx - 1] == 'B':
                res += (l_s - idx - blacks)
                s[idx] = 'B'
                s[idx - 1] = 'W'
                blacks += 1
            idx -= 1
    return res

from collections import deque

ss = deque(S)
length = len(ss)
out = 0
for _ in range(1):
    arr = list(ss)
    out = step(arr, length)
print(out)