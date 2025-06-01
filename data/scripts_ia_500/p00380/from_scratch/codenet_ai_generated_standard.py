import sys
input=sys.stdin.readline

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

N=int(input())
arr=list(map(int,input().split()))
Q=int(input())
swaps=[tuple(map(int,input().split())) for _ in range(Q)]

if is_sorted(arr):
    print(0)
    sys.exit()

bad=set(i for i in range(N-1) if arr[i]>arr[i+1])

for i,(x,y) in enumerate(swaps,1):
    x-=1
    y-=1
    arr[x],arr[y]=arr[y],arr[x]
    for idx in set([x-1,x,y-1,y]):
        if 0<=idx<N-1:
            if arr[idx]>arr[idx+1]:
                bad.add(idx)
            else:
                bad.discard(idx)
    if not bad:
        print(i)
        break
else:
    print(-1)