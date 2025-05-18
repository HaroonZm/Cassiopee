n,a,b,c,d=map(int,input().split())

na=(n//a)*b if n%a==0 else (n//a+1)*b
nc=(n//c)*d if n%c==0 else (n//c+1)*d
print(min(na,nc))