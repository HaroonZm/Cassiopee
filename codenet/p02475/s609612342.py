a,b=map(int,input().split())
print((-1 if a*b<0 else 1)*(abs(a)//abs(b)))