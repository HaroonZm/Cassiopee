l = list(range(1, 100000))
tri_num = set(i*(i+1)//2 for i in range(1, 100000))

while True:
    N = int(input())
    
    if N==0:
        break
    
    b = list(map(int, input().split()))
    
    if sum(b) not in tri_num:
        print(-1)
        continue
    
    ans = 0
    
    while True:
        flag = True
        
        for i in range(len(b)):
            if b[i]!=l[i]:
                flag = False
        
        if flag:
            print(ans)
            break
        
        for i in range(len(b)):
            b[i] -= 1
    
        b.append(len(b));
        b = [bi for bi in b if bi!=0]
        ans += 1
        
        if ans>10000:
            print(-1)
            break