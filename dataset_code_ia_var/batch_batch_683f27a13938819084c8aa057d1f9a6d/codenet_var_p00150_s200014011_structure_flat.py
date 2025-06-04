import math
m = 10000
s = [1 for i in range(m+1)]
s[0] = 0
i = 2
sq = int(math.sqrt(m)) + 1
while i < sq:
    if s[i] != 0:
        j = i*2
        while j < m:
            s[j] = 0
            j += i
    i += 1
ss = []
i = 0
while i <= m:
    if s[i] == 1:
        ss.append(i)
    i += 1
i = 0
j = len(ss) - 1
while i < j:
    ss[i], ss[j] = ss[j], ss[i]
    i += 1
    j -= 1
while 1:
    n = int(input())
    if n == 0:
        quit()
    i = 0
    while i < len(ss) - 1:
        if ss[i] <= n and ss[i] - ss[i+1] == 2:
            print(ss[i+1], ss[i])
            break
        i += 1