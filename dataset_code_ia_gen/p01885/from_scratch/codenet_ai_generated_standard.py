import sys
input=sys.stdin.readline

N,L=map(int,input().split())
drinks=[tuple(map(int,input().split())) for _ in range(N)]
C=[int(input()) for _ in range(N)]

# Precompute prefix sum of sinners' climb for O(1) queries
cumC=[0]*(N+1)
for i in range(N):
    cumC[i+1]=cumC[i]+C[i]

# Sort drinks by efficiency to maximize height each day
# Qualify the order to enable earliest escape:
# Since slides happen only at night, primary climb is Ai, so
# sort by (Ai, Ai-Bi) descending to maximize climb and net progress
order=sorted(range(N),key=lambda i:(drinks[i][0],drinks[i][0]-drinks[i][1]),reverse=True)

height=0
for day in range(1,N+1):
    i=order[day-1]
    Ai,Bi=drinks[i]
    height+=Ai
    if height>=L:
        # Office worker escapes this day after the climb
        # Check if at any night up to previous day sinners caught him
        # At night of day k, sinners climbed cumC[k].
        # After day k, worker at height day stages:
        # height at end of night k is height(day k) - Bi
        # but since he escapes without sliding down, no slide on last day
        conflict=False
        # Check all nights before escape day for conflicts
        # At night k<day, worker height = sum of climbs (Ai) up to k - sum of slides(Bi) up to k
        # Since order fixed, we can maintain these in arrays or recalc:
        # Let's precompute prefix sums of Ai and Bi in order:
        prefixA=[0]*(N+1)
        prefixB=[0]*(N+1)
        for idx in range(N):
            Ai2,Bi2=drinks[order[idx]]
            prefixA[idx+1]=prefixA[idx]+Ai2
            prefixB[idx+1]=prefixB[idx]+Bi2
        # Check for nights 1..day-1
        for k in range(1,day):
            worker_height=prefixA[k]-prefixB[k]
            if worker_height<=cumC[k]:
                conflict=True
                break
        if not conflict:
            print(day)
            exit()
    height-=B_i if day!=N else 0
print(-1)