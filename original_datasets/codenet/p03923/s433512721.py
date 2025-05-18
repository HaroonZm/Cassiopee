n,a=map(int,raw_input().split())
ans=10**12+5
for eat_num in xrange(45):
    if 2**(eat_num-1)>n:break
    time=eat_num*a
    bake=eat_num+1
    l=0;r=n
    while r-l>1:
        m=(r+l)/2
        if m**bake>=n:r=m
        else:l=m
    for surplus in xrange(1,bake+1):
        if r**(bake-surplus) * (r-1)**surplus < n:break
    surplus-=1
    time+=r*(bake-surplus)+(r-1)*surplus
    ans=min(ans,time)
print ans