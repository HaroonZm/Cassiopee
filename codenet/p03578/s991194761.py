N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

def countNumber(LIST):
    cnt = {}
    for l in LIST:
        try:
            cnt[l] += 1
        except KeyError:
            cnt[l] = 1
    return cnt

countD = countNumber(D)
countT = countNumber(T)

flag = True
for i in countT.keys():
    try:
        if countD[i] < countT[i]:
            flag = False
    except KeyError:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')