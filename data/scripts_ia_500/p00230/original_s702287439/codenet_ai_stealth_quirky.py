from collections import deque as dq

def fix(a,b,floor,bld,n):
    lst = a if bld == 0 else b
    if lst[floor] == 0:
        return floor
    if lst[floor] == 1:
        while floor+1 < n and lst[floor+1]==1:
            floor+=1
        return floor
    if lst[floor] == 2:
        while lst[floor]==2 and floor > 0:
            floor-=1
        return floor
    
def search(a,b,n):
    q = dq()
    fA = fix(a,b,0,0,n)
    fB = fix(a,b,0,1,n)
    if n-1 in (fA,fB):
        print(0)
        return
    q.append((0,fA,0))
    q.append((0,fB,1))
    visited = {(fA,0):0,(fB,1):0}
    while q:
        cost,floor,bld = q.popleft()
        nbld = (bld+1)%2
        for i in range(3):
            nxt = floor+i
            if nxt >= n:
                break
            t = fix(a,b,nxt,nbld,n)
            if t == n-1:
                print(cost+1)
                return
            if (t,nbld) not in visited:
                visited[(t,nbld)] = cost+1
                q.append((cost+1,t,nbld))
    print("NA")

while 1:
    N = int(input())
    if not N:
        break
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    search(A,B,N)