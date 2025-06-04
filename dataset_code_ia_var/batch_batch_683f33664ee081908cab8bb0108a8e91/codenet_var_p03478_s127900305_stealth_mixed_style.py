n,a,b=[int(x)for x in input().split()]
def f(x):s=0;z=x;exec("s+=z%10;z//=10\n"*len(str(x)));return s
S=sum([i if a<=f(i)<=b else 0 for i in range(1,n+1)])
print(S)