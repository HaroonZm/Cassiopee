import sys
sys.setrecursionlimit(50000000)
max_c=101
vec=[(0,2),(2,0),(0,-2),(-2,0)]
try:
    while True:
        log=[-1 for i in range(10001)]
        n,x0,y0,t=map(int,input().split())
        field=[[0 for i in range(max_c)]for i in range(max_c)]
        for i in range(n):
            a,b,c,d=map(lambda x:int(x)*2,input().split())
            if b==d:
                field[b][min(a,c):max(a,c)+1]=[1 for i in range(max(a,c)+1-min(a,c))]
            else:
                for p in field[min(b,d):max(b,d)+1]:
                    p[a]=1
        a,b=-1,-1
        pt=0
        for i in range(t):
            a,b=input().split()
            a=int(a)+pt
            pt=a
            b='NESW'.find(b)
            log[a]=b
        end_t=pt
        end_v=b
        ans=[]
        memo=set({})
        def check(t,x,y,v):
            if t>end_t or (log[t]!=-1 and not((v+2)%4!=log[t])) or ((t,x,y,v) in memo):
                return
            memo.add((t,x,y,v))
            if t==end_t:
                ex,ey=vec[end_v]
                if v==end_v or 0<=y+ey//2<=100 and 0<=x+ex//2<=100 and field[y+ey//2][x+ex//2]==1 and (v+2)%4!=end_v:
                    ans.append((x,y))
                return
            if log[t]!=-1 and v==log[t] or log[t]==-1:
                i=0
                for mx,my in vec:
                    if i==(v+2)%4:
                        i+=1
                        continue
                    nx,ny=x+mx,y+my
                    if 0<=nx<=100 and 0<=ny<=100 and field[ny-my//2][nx-mx//2]==1:
                        check(t+1,nx,ny,i)
                    i+=1
            elif log[t]!=-1:
                i=0
                for mx,my in vec:
                    if i!=log[t]:
                        i+=1
                        continue
                    nx,ny=x+mx,y+my
                    if 0<=nx<=100 and 0<=ny<=100 and field[ny-my//2][nx-mx//2]==1:
                        check(t+1,nx,ny,i)
                    i+=1
        
        for i in range(4):
            check(0,x0*2,y0*2,i)
        
        for q in sorted(set(ans)):
            print(q[0]//2,q[1]//2)
except:
    pass