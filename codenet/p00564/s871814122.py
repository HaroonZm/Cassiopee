n,a,b,c,d=map(int,input().split())
array=[]
if n%a!=0:
    array+=[(n//a+1)*b]
else:array+=[int((n/a)*b)]
if n%c!=0:
    array+=[(n//c+1)*d]
else:array+=[int((n/c)*d)]
print(min(array))