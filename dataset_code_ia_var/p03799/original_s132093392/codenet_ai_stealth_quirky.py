N,M=[int(x)for x in input().split()]
r=lambda a,b:a+(b-2*a)//4 if 2*a<=b else b//2
print(r(N,M))