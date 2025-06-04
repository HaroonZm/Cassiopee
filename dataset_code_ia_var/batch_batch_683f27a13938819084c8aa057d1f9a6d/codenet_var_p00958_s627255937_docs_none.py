from math import gcd
m = int(input())
P = [list(map(int, input().split())) for _ in range(m)]
tmp = {}
for i, pi in enumerate(P):
    for j, pj in enumerate(P):
        if i == j:
            break
        x = pi[0] - pj[0]
        y = pi[1] - pj[1]
        k = (x // gcd(x, y), y // gcd(x, y))
        if k in tmp:
            tmp[k].append([pi, pj])
        else:
            tmp[k] = [[pi, pj]]
dic = {}
for t in tmp:
    if len(tmp[t]) == 1:
        continue
    dic[t] = tmp[t]
ans = 0
for d1 in dic:
    line1 = []
    line1.append(dic[d1])
    used1 = [p for pp in dic[d1] for p in pp]
    for d2 in dic:
        tmp2 = []
        for t in dic[d2]:
            if t[0] in used1 or t[1] in used1:
                continue
            tmp2.append(t)
        if len(tmp2) == 1:
            continue
        line2 = line1 + [tmp2]
        used2 = used1 + [p for pp in tmp2 for p in pp]
        for d3 in dic:
            tmp3 = []
            for t in dic[d3]:
                if t[0] in used2 or t[1] in used2:
                    continue
                tmp3.append(t)
            if len(tmp3) == 1:
                continue
            line3 = line2 + [tmp3]
            used3 = used2 + [p for pp in tmp3 for p in pp]
            for d4 in dic:
                tmp4 = []
                for t in dic[d4]:
                    if t[0] in used3 or t[1] in used3:
                        continue
                    tmp4.append(t)
                if len(tmp4) == 1:
                    continue
                line4 = line3 + [tmp4]
                anstmp = 0
                for l in line4:
                    anstmp += len(l) * (len(l) - 1) / 2
                ans = max(anstmp, ans)
print(int(ans))