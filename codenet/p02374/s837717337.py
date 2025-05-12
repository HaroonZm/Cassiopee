N = 10**5
prt = [0]*(N+1)
left = [-1] + [0]*N
right = [-1] + [0]*N
sz = [0] + [1]*N
key = [0]*(N+1)
val = [0]*(N+1)
rev = [0]*(N+1)
 
def update(i, l, r):
    #assert 1 <= i <= N
    sz[i] = 1 + sz[l] + sz[r]
    val[i] = key[i] + val[l] + val[r]
 
def swap(i):
    if i:
        left[i], right[i] = right[i], left[i]
        rev[i] ^= 1
 
def prop(i):
    swap(left[i])
    swap(right[i])
    rev[i] = 0
    return 1
 
def splay(i):
    #assert 1 <= i <= N
    x = prt[i]
    rev[i] and prop(i)
 
    li = left[i]; ri = right[i]
    while x and not left[x] != i != right[x]:
        y = prt[x]
        if not y or left[y] != x != right[y]:
            if rev[x] and prop(x):
                li, ri = ri, li
                swap(li); swap(ri)
 
            if left[x] == i:
                left[x] = ri
                prt[ri] = x
                update(x, ri, right[x])
                ri = x
            else:
                right[x] = li
                prt[li] = x
                update(x, left[x], li)
                li = x
            x = y
            break
 
        rev[y] and prop(y)
        if rev[x] and prop(x):
            li, ri = ri, li
            swap(li); swap(ri)
 
        z = prt[y]
        if left[y] == x:
            if left[x] == i:
                v = left[y] = right[x]
                prt[v] = y
                update(y, v, right[y])
 
                left[x] = ri; right[x] = y
                prt[ri] = x
                update(x, ri, y)
 
                prt[y] = ri = x
            else:
                left[y] = ri
                prt[ri] = y
                update(y, ri, right[y])
 
                right[x] = li
                prt[li] = x
                update(x, left[x], li)
 
                li = x; ri = y
        else:
            if right[x] == i:
                v = right[y] = left[x]
                prt[v] = y
                update(y, left[y], v)
 
                left[x] = y; right[x] = li
                prt[li] = x
                update(x, y, li)
 
                prt[y] = li = x
            else:
                right[y] = li
                prt[li] = y
                update(y, left[y], li)
 
                left[x] = ri
                prt[ri] = x
                update(x, ri, right[x])
 
                li = y; ri = x
 
        x = z
        if left[z] == y:
            left[z] = i
            update(z, i, right[z])
        elif right[z] == y:
            right[z] = i
            update(z, left[z], i)
        else:
            break
 
    update(i, li, ri)
    left[i] = li; right[i] = ri
    prt[li] = prt[ri] = i
    prt[i] = x
 
    rev[i] = prt[0] = 0
 
def expose(i):
    p = 0
    cur = i
    while cur:
        splay(cur)
        right[cur] = p
        update(cur, left[cur], p)
        p = cur
        cur = prt[cur]
    splay(i)
    return i
 
def cut(i):
    expose(i)
    p = left[i]
    left[i] = prt[p] = 0
    return p
 
def link(i, p):
    expose(i)
    expose(p)
    prt[i] = p
    right[p] = i
 
def evert(i):
    expose(i)
    swap(i)
    rev[i] and prop(i)
 
def query(v):
    r = expose(v+1)
    return val[r]
 
def query_add(v, w):
    key[v+1] += w
    expose(v+1)
 
 
readline = open(0).readline
writelines = open(1, 'w').writelines
 
N = int(readline())
for i in range(N):
    k, *C = map(int, readline().split())
    #for c in C:
    #    link(c+1, i+1)
    if k:
        expose(i+1)
        for c in C:
            expose(c+1)
            prt[c+1] = i+1
        right[i+1] = C[0]+1
 
Q = int(readline())
ans = []
for q in range(Q):
    t, *args = map(int, readline().split())
    if t:
        ans.append("%d\n" % query(args[0]))
    else:
        query_add(*args)
writelines(ans)