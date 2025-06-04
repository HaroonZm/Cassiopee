H, W = map(int, input().split())
s = []
for i in range(H):
    s.append(input())
ans = 'Yes'
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            ok = False
            if i != 0:
                if s[i-1][j] == '#':
                    ok = True
            if i != H-1:
                if s[i+1][j] == '#':
                    ok = True
            if j != 0:
                if s[i][j-1] == '#':
                    ok = True
            if j != W-1:
                if s[i][j+1] == '#':
                    ok = True
            if not ok:
                ans = 'No'
print(ans)