n = int(input())
ar = list(map(int,input().split()))
su = [0]*n
su[0]=ar[0]
for i in range(1,n):
    su[i] = ar[i] + su[i-1]

# +
ans1,off = 0,0
for i in range(0,n):
    if i%2 == 0:
        if su[i] + off <= 0:
            ans1 += 1-(su[i]+off)
            off += 1-(su[i]+off)
    else:
        if su[i] + off >= 0:
            ans1 += (su[i]+off+1)
            off -= (su[i]+off+1)

# -
ans2,off = 0,0
for i in range(0,n):
    if i%2 != 0:
        if su[i] + off <= 0:
            ans2 += 1-(su[i]+off)
            off += 1-(su[i]+off)
    else:
        if su[i] + off >= 0:
            ans2 += (su[i]+off+1)
            off -= (su[i]+off+1)
print(min(ans1,ans2))