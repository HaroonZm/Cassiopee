N = int(input())

S = list()
T = list()

for i in range(N):
  s,t = input().split()
  t = int(t)
  S.append(s)
  T.append(t)
  
X = input()

A = T[S.index(X)+1:]
print(sum(A))