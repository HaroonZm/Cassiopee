h,w=map(int,input().split())
a,b=map(int,input().split())
tiles=(h//a)*(w//b)
print(h*w - tiles*a*b)