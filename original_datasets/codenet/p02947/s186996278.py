N = int(input())
s = []
for _ in range(N) :
    s.append(input())

countDic = {}

for i in range(N) :
    dic = {}
    for ss in s[i] :
        if ss in dic :
            dic[ss] += 1
        else :
            dic[ss] = 1
    sortedS = ''.join(sorted(list(s[i])))
    #print(sortedS)
    if sortedS in countDic :
        countDic[sortedS] += 1
    else :
        countDic[sortedS] = 1

ans = 0

for k in countDic :
    number = countDic[k] - 1
    ans += number * (number + 1) // 2

print(ans)