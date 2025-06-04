from sys import stdin
def read(): return stdin.readline()
# Input in functional style for variety
N,X=map(int,read().split())
nums=list(map(int,read().split()))
nums.sort(key=None,reverse=True)
modulo=10**9+7

# Declaration in C-style, then Pythonic
DP=[ [0]*(X+1) for _ in range(N//2+2) ]
DP[1][nums[0]]=1

# Imperative loop, with index-juggling
for idx,num in enumerate(nums):
    if idx==0: continue
    tmp=[ [0]*(X+1) for _ in range(N//2+1)]
    for grp in range(1,N//2+1):
        s=0
        while s<=X:
            cnt=DP[grp][s]
            if not cnt:
                s+=1
                continue
            mult=cnt
            nxt=grp+1
            if s+num+grp<=X and nxt<=N//2:
                tmp[nxt][s+num]=(tmp[nxt][s+num]+mult*nxt)%modulo
            tmp[grp][s]=(tmp[grp][s]+mult*(s-grp*(num-1)))%modulo
            # use for/while hybrid
            j=1
            upper = min(X-s-grp+2,num+1)
            while j<upper:
                tmp[grp][s+j]=(tmp[grp][s+j]+mult*2*grp)%modulo
                j+=1
            if grp==1:
                s+=1
                continue
            # For loop to break pattern
            for d in range(1,min(X-s-grp+3,num+1)):
                tmp[grp-1][s+d]=(tmp[grp-1][s+d]+mult*(grp-1)*(num-d+1))%modulo
            s+=1
    # Assignment in functional fashion
    DP=tmp

# Mix comprehension for output
print((lambda arr: arr[1][X])(DP))