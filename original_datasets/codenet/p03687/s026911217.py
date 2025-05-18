alpha = "abcdefghijklmnopqrstuvwxyz"
s = list(input())
from copy import deepcopy
ans = 10**9
for c in s:
    s_c = deepcopy(s)
    counter = 0
    while set(s_c) != {c}:
        counter += 1
        new = []
        for i in range(len(s_c)-1):
            if s_c[i] == c or s_c[i+1] == c:
                new.append(c)
            else:
                new.append(0)
        s_c = new
    ans = min(ans, counter)
print(ans)