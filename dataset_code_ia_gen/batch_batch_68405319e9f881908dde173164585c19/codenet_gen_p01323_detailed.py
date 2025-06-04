# 解説:
# この問題は、12行×6列のフィールドにブロックが配置されており、
# ルールに従ってブロックの消滅と連鎖を繰り返すものです。
# 主な処理は以下の通りです。
# 1. 同じ色で4つ以上つながっているブロック（お邪魔以外）を探す。
# 2. お邪魔ブロック（O）は隣接する基本色ブロックが消えると一緒に消える。
# 3. 消滅は全て同時に行い、その後ブロックが落下する。
# 4. 落下後も消滅判定を繰り返し、消滅がなければ連鎖終了。
# 
# 実装では以下の関数を用います。
# - bfsで同色連結を探索して消滅ブロックを判定
# - お邪魔ブロックが消えるか判定
# - 落下処理
# - これらを連鎖ごとに繰り返す

import sys
sys.setrecursionlimit(10**7)
from collections import deque

# フィールドの行数・列数
H, W = 12, 6

def solve_field(field):
    chain_count = 0
    
    while True:
        # 消滅対象ブロックを集めるためのセット
        to_erase = set()
        
        visited = [[False]*W for _ in range(H)]
        
        # 1. 同色連結で4つ以上つながるものを探す（お邪魔ブロックOは除く）
        for i in range(H):
            for j in range(W):
                c = field[i][j]
                if c == '.' or c == 'O' or visited[i][j]:
                    continue
                # BFSで同色連結を探索
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                same_color = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W:
                            if not visited[nx][ny] and field[nx][ny] == c:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                same_color.append((nx, ny))
                # 4つ以上つながっていれば消滅対象
                if len(same_color) >= 4:
                    for pos in same_color:
                        to_erase.add(pos)
        
        if not to_erase:
            # 消えるブロックがなければ終了
            return chain_count
        
        # 2. お邪魔ブロックOの消滅判定
        # ・お邪魔ブロックは周囲4方向に基本色ブロックが消滅ブロックの中にあれば消える
        # ・周囲のq基本色4方向を見てto_eraseに含まれていれば消える
        # この消滅も同時に起きるため、繰り返しお邪魔も消す
        changed = True
        while changed:
            changed = False
            for i in range(H):
                for j in range(W):
                    if field[i][j] == 'O' and (i,j) not in to_erase:
                        # 周囲4方向にto_erase内の基本色ブロックがあれば消える
                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            ni, nj = i+dx, j+dy
                            if 0 <= ni < H and 0 <= nj < W:
                                if (ni,nj) in to_erase:
                                    c = field[ni][nj]
                                    # 基本色なら (Oは除く)
                                    if c in ['R','G','B','Y','P']:
                                        to_erase.add((i,j))
                                        changed = True
                                        break
        
        # 3. 消滅処理
        for (i,j) in to_erase:
            field[i][j] = '.'
        
        chain_count += 1
        
        # 4. お邪魔も含めて全ブロックを落下させる
        for col in range(W):
            stack = []
            # 下から上に見て、空きマス以外を集める
            for row in range(H-1, -1, -1):
                if field[row][col] != '.':
                    stack.append(field[row][col])
            # 下から詰める
            for row in range(H-1, -1, -1):
                if stack:
                    field[row][col] = stack.pop(0)
                else:
                    field[row][col] = '.'

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        field = [list(input().rstrip('\n')) for __ in range(H)]
        print(solve_field(field))

if __name__ == '__main__':
    main()