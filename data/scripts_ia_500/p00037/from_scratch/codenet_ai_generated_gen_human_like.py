h_walls = [list(map(int, list(input()))) for _ in range(5)]
v_walls = [list(map(int, list(input()))) for _ in range(4)]

# 格子は5x5区画の境界を表す壁の情報が与えられていると推測
# 横壁は6本あり、5行で与えられるため5行x5列の格子の上端と下端の線が含まれる
# しかしここでは問題文の入力形式に従い、交互に横線と縦線が入力されているように見えるため設定を変更する
walls = []
for i in range(9):
    s = input()
    walls.append(list(map(int,list(s))))

# 横壁行は偶数行インデックス（0,2,4,6,8）
# 縦壁行は奇数行インデックス（1,3,5,7）

H = []
V = []
for i in range(9):
    if i%2 == 0:
        H.append(walls[i])
    else:
        V.append(walls[i])

# 格子のサイズ（区画数）は横壁の横幅で決まる
w = len(H[0]) - 1
h = len(V)

# 東西南北の方向ベクトルと右手をつけた時の回転（時計回り）を定義
dx = [1,0,-1,0] #右、下、左、上
dy = [0,1,0,-1]
# 右に曲がる（方向を時計回りに変える）: d = (d + 1) % 4
# 左に曲がる（反時計回り）: d = (d - 1) % 4

# 点A: (0,0)からスタートし、壁に右手をつけて進む
x,y = 0,0
d = 0 # 0=右向き(東)

path = []

def can_go(nx,ny,direction):
    # nx,ny は通りたいマスの左上点
    # 移動方向によって壁の存在を判定する
    if direction == 0: # 右へ移動するなら、横壁の行(y)の列(x+1)を調べる
        return H[y][x+1] == 0
    elif direction == 2: # 左へ移動するなら、横壁の行(y)の列(x)を調べる
        return H[y][x] == 0
    elif direction == 1: # 下へ移動するなら、縦壁の行(y)の列(x)を調べる
        return V[y][x] == 0
    elif direction == 3: # 上へ移動するなら、縦壁の行(y-1)の列(x)を調べる
        return V[y-1][x] == 0

while True:
    # 右手が壁なら進む方向を左に変え続ける
    # 右手を壁に付けて移動するので、まず右方向の壁を調べ進めるなら進む
    # 右方向の方向は dの次の方向(d+1)%4
    for i in range(4):
        nd = (d + 3) % 4 # 最初は右に手をつけている方向=現在の方向の右側方向
        nd = (d + 1) % 4  # dの右方向
        # 実際には右手の壁を触りながら動くため、右の壁がなければ右に曲がって進む
        # 右手の壁があるか調べ、壁が無ければ回転しないで進める
        # ここは右手の壁がある条件を実装

        # 右手の方向
        right_dir = (d + 1) % 4
        # 右手側の壁の有無を判定
        # 右に壁がなければ進行方向を右に曲げて進む
        nx = x + dx[(d + 1) % 4]
        ny = y + dy[(d + 1) % 4]
        # 現在が格子の内側か判定して壁をチェック
        # 右手に壁があるか判定するには移動先方向の壁の有無ではなく、右側の壁の有無を判定
        # 右手側に壁があるかを判定するために進もうとしている方向の壁をチェックする
        # 右方向の壁が0なら壁なし→右に曲がれる進める
        if (0 <= x < w) and (0 <= y < h):
            if right_dir == 0:  # 右向き
                right_wall = H[y][x+1]
            elif right_dir == 2: # 左向き
                right_wall = H[y][x]
            elif right_dir == 1: # 下向き
                right_wall = V[y][x]
            else: # 上向き
                right_wall = V[y-1][x]
        else:
            right_wall = 1 # 枠外は壁とみなす

        if right_wall == 0:
            # 右に曲がって進む
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]
            path.append("RDLU"[d])
            break
        else:
            # 右に壁があれば，前に行けるかチェック
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx <= w and 0 <= ny < h:
                if d == 0:
                    front_wall = H[y][x+1]
                elif d == 2:
                    front_wall = H[y][x]
                elif d == 1:
                    front_wall = V[y][x]
                else:
                    front_wall = V[y-1][x]
            else:
                front_wall = 1
            if front_wall == 0:
                # 前に進む
                x = nx
                y = ny
                path.append("RDLU"[d])
                break
            else:
                # 前にも壁があれば左に曲がってみる
                d = (d - 1) % 4
    if x == 0 and y == 0 and d == 0 and len(path) > 0:
        break

print("".join(path))