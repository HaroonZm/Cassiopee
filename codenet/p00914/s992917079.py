import itertools
while 1:
    n,k,s=map(int,input().split())
    if n==0:break
    print(sum([1 if sum(i) == s else 0 for i in itertools.combinations(range(1,n+1),k)]))