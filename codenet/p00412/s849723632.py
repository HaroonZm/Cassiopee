n,m = (int(x) for x in input().split())
rane = [[]  for i in range(n)]

def getRane():
    index = 0
    min = 9999
    for i in range(0,n):
        if min > len(rane[i]):
            min = len(rane[i])
            if min == 0:
                return i
            index = i
    return index

for i in range(0,m):
    c,num = (int(x) for x in input().split())
    # 給油終了
    if c == 0:
        num -= 1
        print(rane[num][0])
        rane[num].pop(0)
    # スタンドに入る
    else:
        index = getRane()
        rane[index].append(num)