import sys
input=sys.stdin.readline

N=int(input())
bugs=[tuple(map(int,input().split())) for _ in range(N)]

bugs.sort(key=lambda x: x[1])  # sort by capacity

def can(x):
    # check if we can select x bugs so that total foo / x <= each bug's capacity
    # Select x bugs with smallest foo output among first x bugs
    import heapq
    heap=[]
    sum_a=0
    for i in range(x):
        a,b=bugs[i]
        sum_a+=a
        heapq.heappush(heap,-a)
    if sum_a<=bugs[x-1][1]*x:
        return True
    for i in range(x,N):
        a,b=bugs[i]
        if b<x:
            continue
        # try to improve sum_a by replacing largest a
        if -heap[0]>a:
            sum_a+=a + heap[0]
            heapq.heappop(heap)
            heapq.heappush(heap,-a)
        if sum_a<=b*x:
            return True
    return False

left,right=1,N
ans=0
while left<=right:
    mid=(left+right)//2
    if can(mid):
        ans=mid
        left=mid+1
    else:
        right=mid-1
print(ans)