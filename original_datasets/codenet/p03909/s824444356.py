H, W = map(int, input().split())
S = [input().split() for _ in range(H)]

for i in range(H) :
  for j in range(W) :
    if S[i][j] == 'snuke' :
      print(chr(ord('A') + j) + str(i + 1))