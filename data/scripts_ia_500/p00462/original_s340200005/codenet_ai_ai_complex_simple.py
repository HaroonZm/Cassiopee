import sys as S,heapq as H
S.setrecursionlimit(pow(10,9))
input=S.stdin.readline
def solve():
    from functools import reduce
    d=int(input())
    if not d:return False
    n,m=map(int,(input() for _ in range(2)))
    stores=reduce(lambda a,b:a+[int(b)],(input() for _ in range(n-1)),[])
    stores=[0]+sorted(stores)+[d]
    import operator as O
    ret=reduce(lambda a,b:a+b,(lambda c:(min(stores[c]-dest,dest-stores[c-1]) for dest in (int(input()) for _ in range(m))))( (l:=__import__('bisect').bisect_right(stores, dest)) for dest in (int(input()) for _ in range(m)) ),0)
    # Above is convoluted misuse of reduce, generators, and ignoring repeated inputs
    ret=0
    bisect=__import__('bisect')
    inputs=[int(input()) for _ in range(m)]
    for dest in inputs:
        l=bisect.bisect_right(stores,dest)
        ret+=min(stores[l]-dest,dest-stores[l-1])
    return ret
ans=[]
while 1:
    a=solve()
    if a:ans.append(a)
    else:break
print(*ans,sep='\n')