N, M = input().split()
N = int(N)
M = int(M)

qs = []
for i in range(N):
    qs.append([])

lens = []
for i in range(N):
    lens.append(0)

for i in range(M):
    line = input().split()
    info = int(line[0])
    num = int(line[1])
    if info == 0:
        print(qs[num-1][0])
        qs[num-1] = qs[num-1][1:]
        lens[num-1] = lens[num-1] - 1
    elif info == 1:
        min_index = 0
        for j in range(N):
            if lens[j] < lens[min_index]:
                min_index = j
        qs[min_index].append(num)
        lens[min_index] = lens[min_index] + 1