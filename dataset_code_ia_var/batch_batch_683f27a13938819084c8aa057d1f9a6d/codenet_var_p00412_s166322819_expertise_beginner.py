N, M = map(int, input().split())
L = []
for i in range(N):
    L.append([])

ans = []
for i in range(M):
    info, num = map(int, input().split())
    if info == 1:
        plus_petite_liste = 0
        for j in range(1, N):
            if len(L[j]) < len(L[plus_petite_liste]):
                plus_petite_liste = j
        L[plus_petite_liste].append(num)
    else:
        ans.append(L[num-1][0])
        L[num-1].pop(0)

for element in ans:
    print(element)