# 入力例のように座標系は (x, y) で表され、
# y （行番号）が奇数か偶数かで六角形の南側の隣接関係が変わる。
# この問題のポイントは、建物のある六角形の壁面のうち、
# 外部（建物の塊の外）に接している部分の長さを計算すること。
#
# アプローチ：
# 1. 建物のマップを受け取り、周囲を0で囲んで拡張する。
# 2. 「外部」となる部分を BFS で探索し、外部から建物の隣接する辺をカウントする。この時に壁面の長さを合計していく。
# 3. BFSにより建物の外から到達可能な0の領域（外部空間）を特定し、外部空間と接している建物の壁のみをイルミネーションとしてカウント。
#
# 六角形の隣接関係は y の奇偶で分岐するため、それを反映する。

import sys
from collections import deque

def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    W, H = map(int, input().split())
    # 建物情報を格納（1:建物あり、0:なし）
    grid = [list(map(int, input().split())) for _ in range(H)]
    # 外周の探索のために外周を0で囲う（範囲外は外部とみなす）
    padded = [[0]*(W+2)]
    for row in grid:
        padded.append([0]+row+[0])
    padded.append([0]*(W+2))

    # y 偶奇で隣接判定が異なるため2種類の方向ベクトル
    # 行番号は padded で1始まり。y=1は paddedの1行目、元のgridの0行目に対応
    # y奇数（元の問題の偶数行）とy偶数（元の問題の奇数行）で場合分け
    # 問題の定義より：
    # y奇数の六角形の隣接先：（東、西、北東、北西、南東、南西）
    # ただしここではmapの座標yは1〜H+1なので、元のy=iのparityとは異なるので注意
    # ここでは padded の yを使う
    # padded の y行目が奇数か偶数かで分ける
    # 各六角形の隣接方向は以下のように設定する（xは列、yは行）:
    # y奇数行(1,3,5,...): 隣接座標は
    #   東 (x+1,y), 西 (x-1,y)
    #   北東 (x,y-1), 北西 (x-1,y-1)
    #   南東 (x,y+1), 南西 (x-1,y+1)
    # y偶数行(2,4,6,...): 隣接座標は
    #   東 (x+1,y), 西 (x-1,y)
    #   北東 (x+1,y-1), 北西 (x,y-1)
    #   南東 (x+1,y+1), 南西 (x,y+1)

    # これを反映した隣接座標のリストを用意。
    odd_directions = [(1,0), (-1,0), (0,-1), (-1,-1), (0,1), (-1,1)]
    even_directions = [(1,0), (-1,0), (1,-1), (0,-1), (1,1), (0,1)]

    H_p = H+2
    W_p = W+2
    visited = [[False]*W_p for _ in range(H_p)]

    # BFSで外部空間(0で外からアクセス可能な部分)を探索
    # 外部空間から隣接する建物の壁面を数える
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    result = 0

    while queue:
        y, x = queue.popleft()
        # y,xはpadded座標系
        # 奇数偶数判定は行番号yで
        if y % 2 == 1:
            directions = odd_directions
        else:
            directions = even_directions

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < H_p and 0 <= nx < W_p:
                if padded[ny][nx] == 1:
                    # 建物の壁に接しているため壁面を1m分加算
                    result += 1
                else:
                    # 建物がなく、未訪問なら外部としてBFS続行
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx))

    print(result)

if __name__ == "__main__":
    main()