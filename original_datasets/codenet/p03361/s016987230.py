H, W = map(int, input().split())

#H x Wのマスを全て"."の行列で覆う （H+2 x W+2） 
S1 = [list(map(str,input())) for i in range(H)]
for i in range(H):
    S1[i].insert(0,'#')
    S1[i].append('#')
S = S = [['#'] * (W + 2)] + S1 + [['#'] * (W + 2)]

cnt = 0

for i in range(1,H):
    for j in range(1,W):
        if S[i][j] == '#':
            if S[i-1][j] == S[i][j-1] == S[i][j+1] == S[i+1][j] == '.':
                cnt += 1
if cnt == 0:
    print('Yes')
else:
    print('No')