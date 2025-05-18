import sys
input = sys.stdin.readline
INT_MAX = (1<<31) - 1
_N,num = map(int, input().split())
Q = [list(map(int, input().split())) for i in range(num)]
N = 1<<17
N1 = N - 1
N2 = N1 // 2
ars = 2*N - 1
A = [INT_MAX]*(ars)
L = [-1]*(ars)

def propagate(k):

    if(L[k] == -1):
        return
    left = k*2+1
    right = k*2+2
    if(k < N2):
        A[left] = A[right] = L[left] = L[right] = L[k]
        L[k] = -1
        return
    if(k < N1):
        A[left] = A[right] = L[k]
        L[k] = -1

def update(s,t,x,k,l,r):

    if (r <= s or t <= l):
        return
    if (s <= l and r <= t):
        A[k] = x
        if(k < N1):
            L[k] = x
        return

    propagate(k)
    mid = (l+r)//2
    left = k*2 + 1
    right = k*2 + 2
    update(s, t, x, left, l, mid)
    update(s, t, x, right, mid, r)

    A[k] = min(A[left], A[right])

def find(s,t,k,l,r):

    if (r <= s or t <= l):
        return INT_MAX

    if(s <= l and r <= t):
        return A[k]

    propagate(k)
    mid = (l+r)//2
    left = k*2 + 1
    right = k*2 + 2
    v_left = find(s, t, left, l, mid)
    v_right = find(s, t, right, mid, r)
    return min(v_left,v_right)

res = []
for q in Q:
    # update
    if(q[0]==0):
        update(q[1],q[2]+1,q[3],0,0,N)
    # find
    else:
        res.append(find(q[1],q[2]+1,0,0,N))

print("\n".join([str(r) for r in res]))