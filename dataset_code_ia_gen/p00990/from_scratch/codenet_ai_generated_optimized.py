n=int(input())
ID=input()
m=int(input())
candidates=list(map(int,input().split()))

positions=[i for i,ch in enumerate(ID) if ch=='*']

def digit_value(d,k): # d:int digit, k: position from right (1-based)
    if k%2==0:
        v=d*2
        if v>=10:
            v=(v//10)+(v%10)
        return v
    else:
        return d

fixed_sum=0
length=n
for i,ch in enumerate(ID):
    if ch!='*':
        pos=length - i
        fixed_sum+=digit_value(int(ch),pos)

rem_count=len(positions)
# precompute values for candidates per position
vals=[[digit_value(d,length - p) for d in candidates] for p in positions]

dp=[0]*10
dp[0]=1

for i in range(rem_count):
    ndp=[0]*10
    for mod in range(10):
        if dp[mod]==0:
            continue
        for v in vals[i]:
            ndp[(mod+v)%10]+=dp[mod]
    dp=ndp

rem=(10-(fixed_sum%10))%10
print(dp[rem])