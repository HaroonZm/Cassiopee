S=input()
w=int(input())
i=0
ans=""
while i<len(S):
    ans+=S[i]
    i+=w
print(ans)