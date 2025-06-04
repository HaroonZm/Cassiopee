N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

def countNumber(LIST):
    cnt = {}
    for l in LIST:
        if l in cnt:
            cnt[l] += 1
        else:
            cnt[l] = 1
    return cnt

countD = countNumber(D)
countT = countNumber(T)

flag = True
for i in countT:
    if i not in countD or countD[i] < countT[i]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')