n,a,b,c,d=map(int,input().split())
na=sum([b for _ in range(-(-n//a))])
nc=sum([d for _ in range(-(-n//c))])
print((lambda x,y:min(x,y))(na,nc))