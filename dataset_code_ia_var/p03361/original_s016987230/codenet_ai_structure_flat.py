H, W = map(int, input().split())
S1 = []
for i in range(H):
    row = list(input())
    row.insert(0, '#')
    row.append('#')
    S1.append(row)
top_bottom = ['#'] * (W + 2)
S = [top_bottom[:]]
for row in S1:
    S.append(row)
S.append(top_bottom[:])
cnt = 0
i = 1
while i < H:
    j = 1
    while j < W:
        if S[i][j] == '#':
            if S[i-1][j] == '.' and S[i][j-1] == '.' and S[i][j+1] == '.' and S[i+1][j] == '.':
                cnt += 1
        j += 1
    i += 1
if cnt == 0:
    print('Yes')
else:
    print('No')