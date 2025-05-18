while 1:
    x,y,s = map(int,input().split())
    if x==y: break
    ans = 0
    
    for i in range(1,s):
        for j in range(i,s):
            if (i+j+(i*x)//100+(j*x)//100)==s:
                tmp = i+j+(i*y)//100+(j*y)//100
                if tmp>ans:
                    ans = tmp
    
    print(ans)