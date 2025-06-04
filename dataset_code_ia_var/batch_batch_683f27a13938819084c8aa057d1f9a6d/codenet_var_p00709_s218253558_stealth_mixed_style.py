import sys
def getinput():
    return sys.stdin.readline()
syswrite = sys.stdout.write

def process():
    # style 1: tuple unpack
    wh = getinput()
    if not wh:
        return False
    (w, h) = tuple(map(int, wh.split()))
    if w == 0:
        return False
    # style 2: comprehension, mixed with imperative
    mp = []
    push = mp.append
    for i in range(h):
        vals = list(map(int, input().split()))
        push(vals)
    # style 3: C-like loop
    c = [[0 for _ in range(w)] for _ in range(h)]
    for j in range(w):
        x = 0
        for i in range(h-1, -1, -1):
            x = (x+1)*mp[i][j] if mp[i][j] else 0
            c[i][j]=x
    # style 4: functional where possible
    d = [[0]*w for _ in range(h)]
    e = [ [0]*w for x in range(h)]
    for idx, row in enumerate(c):
        st=[]
        j=0
        while j<w:
            cx=row[j]
            last=j
            while st and cx<=st[-1][0]:
                (p, k)=st.pop()
                last=k
                delta=min(j-k,p)
                for ex in range(k, j-delta+1):
                    d[idx][ex]=max(d[idx][ex], delta)
            st.append((cx,last))
            j+=1
        while st:
            p,k=st.pop()
            delta=min(w-k,p)
            if delta:
                for ex in range(k, w-delta+1):
                    d[idx][ex]=max(d[idx][ex], delta)
        st.append((w,0))
    # style 5: interleaved one-liners and blocks
    S, Z = [], [0]*(w*h); ALL = 0
    for i in range(h):
        for j in range(w):
            ALL |= (1<<(i*w+j)) if mp[i][j] else 0
            if e[i][j]<d[i][j]:
                S+=[i*w+j]; Z[i*w+j]=d[i][j]
            newe = max(e[i][j], d[i][j])
            e[i][j]=newe
            if newe>1:
                if i+1<h: e[i+1][j]=max(e[i+1][j], newe-1)
                if j+1<w: e[i][j+1]=max(e[i][j+1], newe-1)
                if i+newe-1<h and j+newe-1<w: e[i+newe-1][j+newe-1]=max(e[i+newe-1][j+newe-1],1)
    sn = len(S)
    L = max(w,h)
    t = [0]*(L+1)
    for dsz in range(1, L+1):
        v=0
        for ix in range(dsz):
            for jx in range(dsz):
                v|=1<<(ix*w+jx)
        t[dsz]=v
    bs=[0]*sn; cs=[0]*sn
    for k in range(sn):
        s = S[k]
        bs[k]=t[Z[s]]<<s
        cs[k]=1<<s
    # style 6: nested function, tabulation
    mem=[dict() for _ in range(sn)]
    def rec(i, st):
        if i==sn:
            return 0 if st==ALL else w*h
        if st in mem[i]: return mem[i][st]
        rr=w*h
        if st&cs[i]: rr=min(rr,rec(i+1,st))
        if st&bs[i]!=bs[i]:
            rr=min(rr, rec(i+1, st|bs[i])+1)
        mem[i][st]=rr
        return rr
    syswrite('%d\n'%rec(0,0))
    return True

while process():
    pass