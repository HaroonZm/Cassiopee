H,W = map(int, input().split())

A = [[0 for i in range(W)] for j in range(H)]

for i in range(H):
    A[i] = list(map(int, input().split()))

# 最小のコスト
Res = [[[float('Inf') for i in range(W * H)] for j in range(H)] for k in range(W)]
Res[0][0][0] = 0

for l in range(1, W*H):
    for x in range(W):
        # 探索する意味がない範囲
        if x > l:
            break
        for y in range(H):
            # 探索する意味がない範囲
            if x + y > l:
                break
            
            # 左
            if x != 0: 
                if Res[x-1][y][l] > Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y][x-1]:
                    Res[x-1][y][l] = Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y][x-1]
                
            # 右
            if x != (W-1):
                # print(x, y, l)
                if Res[x+1][y][l] > Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y][x+1]:
                    Res[x+1][y][l] = Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y][x+1]
                    
            # 上
            if y != 0:
                if Res[x][y-1][l] > Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y-1][x]:
                    Res[x][y-1][l] = Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y-1][x]
                        
            # 下
            if y != (H-1):
                if Res[x][y+1][l] > Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y+1][x]:
                    Res[x][y+1][l] = Res[x][y][l-1] + ((l - 1) * 2 + 1) * A[y+1][x]

print(min(Res[W-1][H-1]))