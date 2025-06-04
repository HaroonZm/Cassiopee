N=int(input())
S=input()
ans=0
i=0
while i<N-1:
    if (S[i]=='O' and S[i+1]=='X') or (S[i]=='X' and S[i+1]=='O'):
        ans+=1
        i+=2
    else:
        i+=1
print(ans)