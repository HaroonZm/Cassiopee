H,W = map(int,input().split())

s = [input() for i in range(H)]

def draw(i,j):
	if j>0 and s[i][j-1] == "#":
		return "Yes"
	if j<W-1 and s[i][j+1] == "#":
		return "Yes"
	if i>0 and s[i-1][j] == "#":
		return "Yes"
	if i<H-1 and s[i+1][j] == "#":
		return "Yes"
	return "No"

ans = "Yes"
for i in range(H):
	for j in range(W):
		if s[i][j] == "#":
			ans = draw(i,j)
			if ans == "No":
				print(ans)
				exit()

print(ans)