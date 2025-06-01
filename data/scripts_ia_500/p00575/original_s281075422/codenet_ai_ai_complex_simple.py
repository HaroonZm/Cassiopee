from functools import reduce
A,B,C=map(int,input().split())
def f(t):
    i,s=0,0
    def g(_):
        nonlocal i,s
        i+=1
        s+=A
        if s>=C: raise StopIteration(i)
        if i%7==0:
            s+=B
            if s>=C: raise StopIteration(i)
    try:
        reduce(lambda _,__:g(None),range(10**9))
    except StopIteration as e:
        print(e.value)
f((A,B,C))