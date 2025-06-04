def f(): a=int(input().split()[0]);return [lambda:sum(map(int,input().split())) for _ in range(a)]
res=[]
for func in f():
    res.append(func())
print((lambda l:max(l))(res))