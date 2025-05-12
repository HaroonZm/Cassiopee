N = int(input())
Xsize = 1001 # 0-1000
Ysize = 1001 # 0-1000
Data = [[0]*(Xsize) for _ in range (Ysize)]
Tmp  = [[0]*(Xsize) for _ in range (Ysize)]
Ans  = [[0]*(Xsize) for _ in range (Ysize)]

for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    Data[y1][x1] += 1
    Data[y1][x2] -= 1
    Data[y2][x1] -= 1
    Data[y2][x2] += 1

#x方向の累積和 
for y in range(Ysize):
    Tmp[y][0] = Data[y][0]
    for x in range(1,Xsize):
        Tmp[y][x] = Data[y][x] + Tmp[y][x-1]
#y方向の累積和 
for x in range(Xsize):
    Ans[0][x] = Tmp[0][x]
    for y in range(1,Ysize):
        Ans[y][x] = Tmp[y][x] + Ans[y-1][x]
#最大値
ans = 0
for y in range(Ysize):
    ans = max(ans,max(Ans[y]))
print(ans)