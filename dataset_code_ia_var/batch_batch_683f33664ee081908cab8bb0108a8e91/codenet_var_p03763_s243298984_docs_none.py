N=int(input())
S=[input() for s in range(N)]
alphabet="abcdefghijklmnopqrstuvwxyz"
A=[[0 for x in range(len(alphabet))]for y in range(N)]
for i in range(N):
  for j in range(len(S[i])):
    a=alphabet.index(S[i][j])
    A[i][a]+=1
ans=[]
A=list(zip(*A))
for i in range(len(alphabet)):
  a=min(A[i])
  ans.append(alphabet[i]*a)
print("".join(ans))