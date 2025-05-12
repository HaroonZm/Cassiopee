a,s=map(int,input().split())
if a*s>=0:
    print(a//s)
else:
    print(-(abs(a)//abs(s)))