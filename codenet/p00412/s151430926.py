N,M = [int(i) for i in input().split()]
table = [[] for i in range(N)]

for l in range(M):
    command,num = [int(i) for i in input().split()]
    if command == 0:
        print(table[num-1].pop(0))
    else:
        minSize = 10000
        minId = -1
        for i in range(N):
            if len(table[i]) < minSize:
                minSize = len(table[i])
                minId = i
        #print(minId,num)
        table[minId].append(num)