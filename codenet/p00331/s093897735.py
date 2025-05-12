h,r=map(int,input().split())
if h<0:
    print(-1 if h+r<0 else 0 if h+r==0 else 1)
else:
    print(1)