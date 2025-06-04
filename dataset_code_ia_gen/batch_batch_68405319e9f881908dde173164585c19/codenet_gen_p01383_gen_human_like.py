import sys
input=sys.stdin.readline

M,N,K=map(int,input().split())
w=[0]+[int(input()) for _ in range(N)]
a=[int(input()) for _ in range(K)]

# For each ball, record positions of future accesses
positions=[[] for _ in range(N+1)]
for i,v in enumerate(a):
    positions[v].append(i)

# For each ball, maintain an index to the next use position
next_use_idx=[0]*(N+1)

cache=[-1]*M  # cache[i] = ball in box i or -1 if empty
pos_in_cache=[-1]*(N+1)  # pos_in_cache[ball] = index of box or -1 if not in cache

ans=0

for i in range(K):
    ball=a[i]
    # Advance next_use_idx for current ball
    next_use_idx[ball]+=1

    if pos_in_cache[ball]!=-1:
        # ball is already in cache, no cost
        continue

    # ball not in cache, miss: need to put in cache
    # Find empty box if any
    empty_idx=-1
    for idx in range(M):
        if cache[idx]==-1:
            empty_idx=idx
            break

    if empty_idx!=-1:
        # Use empty box
        cache[empty_idx]=ball
        pos_in_cache[ball]=empty_idx
        ans+=w[ball]
    else:
        # Need to evict a ball
        # For each ball in cache, find next use position
        # If no next use, next use = infinity
        max_next_use=-1
        evict_idx=-1
        for idx in range(M):
            b=cache[idx]
            nxt=positions[b][next_use_idx[b]] if next_use_idx[b]<len(positions[b]) else 10**9
            if nxt>max_next_use:
                max_next_use=nxt
                evict_idx=idx
        # Evict ball
        evicted_ball=cache[evict_idx]
        pos_in_cache[evicted_ball]=-1

        # Put new ball
        cache[evict_idx]=ball
        pos_in_cache[ball]=evict_idx
        ans+=w[ball]

print(ans)