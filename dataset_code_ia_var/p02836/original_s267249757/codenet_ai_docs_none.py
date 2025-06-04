S=input()
l=0
r=len(S)-1
ans=0
while l<r:
    if S[l]!=S[r]:
        ans+=1
    l+=1
    r-=1
print(ans)