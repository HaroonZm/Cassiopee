N=int(input())
S=list(input().strip())
cnt1=0
cnt2=1
stamp_0x=0
while cnt1<N:
    if cnt1<N-1:
        if S[cnt1]!=S[cnt2]:
            stamp_0x+=1
            cnt1+=2
            cnt2+=2
        else:
            cnt1+=1
            cnt2+=1
            continue
    else:
        cnt1+=1
print(stamp_0x)