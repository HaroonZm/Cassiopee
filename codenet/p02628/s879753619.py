N,K = map(int,input().split())
L=list(map(int,input().split()))
S=0
for i in range (K):
  S+=min(L)
  L.remove(min(L))
print(S)