import sys

def read_dims():
    tokens = sys.stdin.readline().split()
    if len(tokens) != 2: raise Exception("Dims input error")
    return tuple(map(int, tokens))
H, W = read_dims()

C=[]; addrow=C.append
for i in range(H):
    dat=sys.stdin.readline().split()
    addrow([int(x) for x in dat])

dp=[]
for h in range(H):
    row = []
    for w in range(W+1):
        v = 0
        if w != W:
            if C[h][w]==1:
                v=0
            elif not h:
                v=1
            else:v = dp[h-1][w]+1
        row.append(v)
    dp.append(row)

ans=0
for idx,row in enumerate(dp):
    stack=[[-1,0]]
    for w in range(W+1):
        curH = row[w]
        while stack[-1][1]>curH:
            left, hh = stack.pop()
            area = (w-left-1)*hh
            if area>ans: ans=area
        stack.append([w,curH]) if curH>=stack[-1][1] else stack.append([w,curH])
print(ans)