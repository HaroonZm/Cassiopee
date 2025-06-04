H,W = map(int,input().split())
s = [input() for i in range(H)]
ans = "Yes"
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            if j>0 and s[i][j-1] == "#":
                ans = "Yes"
            elif j<W-1 and s[i][j+1] == "#":
                ans = "Yes"
            elif i>0 and s[i-1][j] == "#":
                ans = "Yes"
            elif i<H-1 and s[i+1][j] == "#":
                ans = "Yes"
            else:
                ans = "No"
                print(ans)
                exit()
print(ans)