w,h,x,y,r = map(int, input().split())
a = w - r
b = h - r
if r <= x <= a and r <= y <= b:
    print("Yes")
else:
    print("No")