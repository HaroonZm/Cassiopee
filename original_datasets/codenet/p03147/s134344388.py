#ABC116-C
n = int(input())
h = list(map(int,input().split()))
kadan = [0 for _ in range(n)]
cnt = 0
tf = [False for _ in range(n)]

for i in range(1,10**5):
    cnt += 1
    #print('cnt:',cnt)
    #print('tf:',tf)
    #print('kadan:',kadan)
    flg = False
    for j in range(n):
        if tf[j] == False:
            flg = True
            if kadan[j] == h[j]:
                tf[j] = True
            else:    
                kadan[j] += 1
        elif tf[j] == True and flg == False:
            pass
        else:
            break
            
    if not False in tf:
        break
print(cnt-1)