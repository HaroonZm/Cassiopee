h,w = map(int,input().split())
a,b = map(int,input().split())
rh,rw = h%a, w%b
print(rh*w + rw*h - rh*rw)