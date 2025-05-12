h,w = map(int,input().split())
a,b = map(int,input().split())
print(h*w-(a*(h//a)*b*(w//b)))