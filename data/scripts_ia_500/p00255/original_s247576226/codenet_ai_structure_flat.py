while 1:
    n=int(input())
    if n==0:
        break
    p=list(map(int,input().split()))
    j=list(map(int,input().split()))
    j.sort()
    sump=sum(p)
    sarary=sump*n
    i=0
    while i<n-1:
        sump+=j.pop()
        n-=1
        sara_check=sump*n
        if sara_check>sarary:
            sarary=sara_check
        i+=1
    print(sarary)