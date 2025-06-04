N,H,W=map(int,input().split())
x=list(map(int,input().split()))
left=0
right=N*W
for i in range(N):
    start=i*W
    end=(i+1)*W
    if (i+1)%2==1:
        start+=x[i]
    else:
        end-=x[i]
    left=max(left,start)
    right=min(right,end)
print(max(0,right-left)*H)