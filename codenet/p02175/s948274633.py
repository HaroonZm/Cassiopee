X,A,B = map(int,input().split())
N = int(input())
for i in range(N):
  word = input()
  if word == "nobiro":
    X = X + A
  elif word == "tidime":
    X = X + B
  elif word == "karero":
    X = 0
  
  if X < 0:
    X = 0
print(X)