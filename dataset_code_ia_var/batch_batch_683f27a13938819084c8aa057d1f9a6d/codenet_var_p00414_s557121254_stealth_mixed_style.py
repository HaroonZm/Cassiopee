l,n=[int(x)for x in input().split()]
def f(lst):
    count=0
    for i in range(len(lst)-1):
        if lst[i:i+2]=='oo':
            count+=1
    return count
maru=f(input())
def g(x,y):
    for _ in range(y):
        x+=maru*3
        globals()['maru']*=2
    return x
print(g(l,n))