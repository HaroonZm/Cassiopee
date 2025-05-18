from collections import deque

N, M = map(int, input().split())
S = input()[::-1] +'1'*M

if M >= N:
  print(N)
  exit()
  
q = deque([])

i = 0
j = 0
while i < N:
  f = 0
  for k in range(i+M,j,-1):
    if S[k] == '0':
      f = 1
      break
  j = i + M
  q.appendleft(k-i)
  i = k
  if f == 0:
    print(-1)
    exit()

print(' '.join(map(str, q)))