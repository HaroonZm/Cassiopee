import sys
input=sys.stdin.readline

N,M,C=map(int,input().split())
l=list(map(int,input().split()))

color_balls=[[] for _ in range(C)]
for _ in range(N):
    c,w=map(int,input().split())
    color_balls[c-1].append(w)

candidates=[]
for i in range(C):
    balls=color_balls[i]
    if not balls or l[i]==0:
        continue
    balls.sort(reverse=True)
    take=min(l[i], len(balls))
    candidates.extend(balls[:take])

candidates.sort(reverse=True)
print(sum(candidates[:M]))