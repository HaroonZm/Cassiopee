w,h,x,y,r = map(int,input().split())
if (x + r) <= w and x >= r and (y + r) <= h and y >= r:
    print("Yes")
else:
    print("No")