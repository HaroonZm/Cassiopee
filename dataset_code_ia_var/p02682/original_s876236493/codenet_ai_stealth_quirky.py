(a,b,c,k),Z=map(int,input().split())+[0]
while 1:
    if k<=a:Z=k;break
    if k<=a+b:Z=a;break
    Z=a-(k-(a+b));break
print(Z)