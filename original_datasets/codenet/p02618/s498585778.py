import numpy as np
import sys
read = sys.stdin.read

D = int(input())
CS = np.array(read().split(), np.int32)
C = CS[:26]
S = CS[26:].reshape((-1, 26))
del CS

last = np.zeros((26, ))
ans = []

def getContestType_at_d(d):
    s = -10000000
    for i in range(26):
        mask = np.ones((26, ))
        mask[i] = 0
        tmp = S[d][i] - np.sum(C * (d + 1 - last) * mask)
        if s < tmp:
            s = tmp
            t = i

    last[t] = d + 1

    return t + 1, s
#score = 0
for d in range(D):
    t, _ = getContestType_at_d(d)
    ans.append(t)
    #score += s
    #print('score:', score)

print('\n'.join(map(str, ans)))