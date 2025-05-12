def t2s(t):
    h = t[:2]
    m = t[3:5]
    s = t[6:]
    return int(h)*3600+int(m)*60+int(s)

while (True):
    n = int(input())
    c = [0 for i in range(24*3600+1)]
    if (n == 0):
        break
    for i in range(n):
        tt = input()
        c[t2s(tt[:8])] += 1
        c[t2s(tt[9:])] -= 1
    cc = [0]
    for i in range(len(c)):
        cc.append(cc[-1] + c[i])
    print(max(cc))