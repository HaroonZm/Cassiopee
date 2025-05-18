while 1:
    n=int(input())
    if n==0:
        break
    x=[int(input())for i in range(n)]
    x.sort()
    s=sum(x)-(x[0]+x[-1])
    print(s//(n-2))