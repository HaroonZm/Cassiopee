N,M,C = map(int,input().split())
colors = [int(l) for l in input().split()]
ball = []
#print(len(colors),colors)

for _ in range(0,N):
    c,w = map(int,input().split())
    ball.append([c,w])

ball.sort(key= lambda x:x[1]) #価値でソートした
ball.reverse()
#print(ball)

take = 0 #ボール取った
cost = 0 #合計金額
i = 0 #リストのナンバリング

while (take <= M - 1) and (i <= N - 1):
    if colors[ball[i][0] - 1] == 0:
        i += 1
        #print(i)
        continue
    else:
        cost = cost + ball[i][1]
        colors[ball[i][0] - 1] = colors[ball[i][0] - 1] -1
        take += 1
        i += 1
        #print(i)

print(cost)