# 入力
X,Y,Z=map(int,input().split())

N=1
while True:
  if N*Y+(N+1)*Z>X:
    break
  else:
    N+=1

# 出力
print(N-1)