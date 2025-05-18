while True:
    n = int(input())
    if n==0:
        break
    w = [len(input()) for i in range(n)]
    a = [5,7,5,7,7]
    ans = n+1
    for i in range(n):
        k,s = 0,0
        for j in range(i,n):
            s += w[j]
            if s==a[k]:
                s,k=0,k+1
            elif s>a[k]:
                break
            if k==5:
                ans = min(ans,i+1)
                break
    print(ans)