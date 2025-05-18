#agc17-b
n,a,b,c,d=map(int,input().split())
ans='NO'
maxi=a+d*(n-1)
mini=a+c*(n-1)
if mini<=b<=maxi:
    ans='YES'

else:
    for i in range(1,n):
        maxi=maxi-d-c
        mini=mini-c-d
        if mini<=b<=maxi:
            ans='YES'
            break

print(ans)