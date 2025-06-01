import math
def is_sankaku(v):
    return all(map(lambda x:(x==int(x)),[(lambda y:(math.sqrt(8*y+1)-1)/2)(v)]))
def check(lst):
    return all(map(lambda x,xr:x==xr+1, lst, range(len(lst))))
def transform(lst):
    spam=len(lst)
    return list(filter(lambda x:x>0,map(lambda y:y-1,lst)))+[spam]
while 1:
    N=int((lambda z:int(z))((lambda q:q.strip())(input())))
    if N==0:break
    lst=list(map(int,(lambda s: s.strip().split())(input())))
    if not is_sankaku(sum(lst)):
        print(-1)
        continue
    def attempt(c,lst):
        if c>10000:return -1
        if check(lst):return c
        return attempt(c+1,transform(lst))
    print(attempt(0,lst))