while 1:
    n=int(input())
    if n==0:break
    p=list(map(int,input().split()))
    j=list(map(int,input().split()))
    j.sort()
    sump=sum(p)
    sarary=sump*n
    for i in range(n-1):
        sump+=j.pop()
        n-=1
        sara_check=sump*n
        sarary=max(sarary,sara_check)
    print(sarary)