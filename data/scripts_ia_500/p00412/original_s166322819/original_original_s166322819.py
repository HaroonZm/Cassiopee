N, M = map(int, input().split())
L = [[] for i in range(N)]
ans = []
for i in range(M) :
    info, num = map(int, input().split())
    
    if info == 1 :
        x = 0
        for j in range(1, N) :
            if len(L[j]) < len(L[x]) :
                x = j
        L[x].append(num)
    else :
        ans.append(L[num-1][0])
        del L[num-1][0]
print(*ans, sep='\n')