h, w, d = map(int, input().split())
index = [(0,0) for x in range(h*w+1)]
for i in range(1,h+1):
    col = list(map(int, input().split()))
    for j in range(1,w+1):
        index[col[j-1]] = (i, j)

memo = [0 for x in range(h*w+1)]
l = 0
for l in range(1, h*w+1-d):
    memo[l+d] = memo[l] + abs(index[l+d][0] - index[l][0]) + abs(index[l+d][1]-index[l][1])

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(memo[r]-memo[l])