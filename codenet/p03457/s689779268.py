t, x, y = 0, 0, 0
N = int(input())
info = []
for i in range(N):
    infocstr = input().split()
    infoc = []
    for num in infocstr:
        infoc.append(int(num))
    info.append(infoc)
    
for infoi in info:
    time = infoi[0] - t
    need = abs(x-infoi[1])+abs(y-infoi[2])
    d = time - need
    if d < 0 or d % 2 == 1:
        print('No')
        break
    t, x, y = infoi[0], infoi[1], infoi[2]
        
else:
    print('Yes')