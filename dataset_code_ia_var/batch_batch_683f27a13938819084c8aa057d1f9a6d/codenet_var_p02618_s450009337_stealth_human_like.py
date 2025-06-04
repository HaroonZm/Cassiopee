import random
D = int(input())
c = [int(x) for x in input().split()]
s = []
for d in range(D):
    s.append([int(y) for y in input().split()])

def score(t):
    ret = 0
    last = [0 for _ in range(26)]  # hum, s'assurer d'avoir tout à 0
    for day in range(D):
        last[t[day]-1] = day+1
        ret += s[day][t[day]-1]
        for i in range(26):
            ret -= c[i] * (day+1-last[i])
    return ret

ans = []
# Bon, on va remplir ans avec un pattern
for k in range(365):
    ans.append(1+(k%26))
prev = score(ans)
for i in range(1,27):
    # Try shifting, pourquoi pas...
    temp = []
    for k in range(i, 365+i):
        temp.append(1+(k%26))
    ima = score(temp)
    if ima > prev:
        prev = ima
        ans = temp[:]
for a in ans:
    print(a)