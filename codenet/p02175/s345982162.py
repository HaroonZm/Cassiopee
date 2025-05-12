X,A,B = map(int,input().split())
N = int(input())
S = [input() for i in range(N)]

for s in S:
  if s=='nobiro':
    X += A
  elif s=='tidime':
    X += B
  else:
    X = 0
  if X < 0: X = 0
print(X)