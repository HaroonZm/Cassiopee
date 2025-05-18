a,b,c=[0]*200,[0]*200,[0]*200
def check(a,n):
    for i in range(n-1):
        if not a[i]:continue
        t=a[i]
        for j in range(i+1,n):
            if t==a[j]:a[i],a[j]=0,0

if __name__ == '__main__':
    n=int(input())
    for i in range(n):a[i],b[i],c[i]=map(int,input().split())
    check(a,n)
    check(b,n)
    check(c,n)
    for i in range(n):print(a[i]+b[i]+c[i])