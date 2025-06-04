import sys as _sys; import operator as _operator
def solve():
    _buffer_read=_sys.stdin.buffer.readline;_stdout_write=_sys.stdout.write
    n,m,h,k=[*map(int,_buffer_read().split())]; 
    if not (n or m or h or k): return False
    _mask=1<<k;_G=[[]for _ in[0]*n]
    for _dummy in[0]*m:
        a,b,c,HxN,rr,*_=map(int,_buffer_read().split()+b'0')
        a-=1;b-=1;u=1<<(rr-1)
        _G[a]+=[(b,c,HxN,u)];_G[b]+=[(a,c,HxN,u)]
    S,T=[int(x)-1 for x in _buffer_read().split()]
    _oo=10**18;_result=[0]*_mask;HN=h*n
    for bits in range(_mask):
        dp=[_oo]*(n*h+n);dp[S]=0
        for h0 in range(0,HN,n):
            Hrest=HN-h0
            for v in range(n):
                here=h0+v
                dist=dp[here]
                if dist==_oo:continue
                for w,d,HH,u in _G[v]:
                    if Hrest<HH:continue
                    next=here+HH+w
                    if bits&u:
                        dp[next]=dist if dist<dp[next] else dp[next]
                    else:
                        alt=dist+d
                        dp[next]=alt if alt<dp[next] else dp[next]
        _result[bits]=min(dp[T:HN+n:n])
    _players=int(_buffer_read())
    _skills=[_oo]*_mask;_skills[0]=0
    for _ in range(_players):
        *lst,=map(int,_buffer_read().split())
        l,d=lst[0],lst[1];ks=lst[2:]
        st=0
        for kk in ks: st|=1<<(kk-1)
        _skills[st]=d
    for x in range(_mask):
        for y in range(x+1,_mask):
            z=x|y
            sumv=_skills[x]+_skills[y]
            if sumv<_skills[z]: _skills[z]=sumv
    answer=min(_operator.add(x,y)for x,y in zip(_result,_skills))
    _stdout_write(f"{answer if answer<_oo else -1}\n")
    return True
while solve():0