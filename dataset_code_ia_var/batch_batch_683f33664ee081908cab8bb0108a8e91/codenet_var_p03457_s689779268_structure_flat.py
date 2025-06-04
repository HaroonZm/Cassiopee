t = 0
x = 0
y = 0
N = int(input())
info = []
i = 0
while i < N:
    infocstr = input().split()
    infoc = []
    j = 0
    while j < len(infocstr):
        infoc.append(int(infocstr[j]))
        j += 1
    info.append(infoc)
    i += 1

k = 0
flg = True
while k < len(info):
    infoi = info[k]
    time = infoi[0] - t
    need = abs(x - infoi[1]) + abs(y - infoi[2])
    d = time - need
    if d < 0 or d % 2 == 1:
        print('No')
        flg = False
        break
    t = infoi[0]
    x = infoi[1]
    y = infoi[2]
    k += 1
if flg:
    print('Yes')