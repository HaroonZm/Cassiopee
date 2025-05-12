H,W = map(int,input().split())
N = int(input())
Data = list(map(int,input().split()))
Ans = [[0]*W for _ in range(H)]

w = 0
h = 0
direction = 1
num = 0
for d in Data:
    num += 1
    for _ in range(d):
        Ans[h][w] = num

        if direction == 1:
            if w == W-1:
                direction = 2
                h += 1
            else:
                w += 1
        else:
            if w == 0:
                direction = 1
                h += 1
            else:
                w -= 1

for h in range(H):
    for w in range(W):
        print( Ans[h][w], end = ' ')
    print()