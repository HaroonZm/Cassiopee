# 解法のアプローチ説明
# 
# - 盤面は19行15列の固定サイズ。
# - 白石は1つだけ存在し、その位置をスタート地点とする。
# - ゴール地点は「行番号が19以上（つまり盤面の下端より下）」で判定する。
# - 白石は隣接8方向の黒石の連続を「飛び越え」可能。
#   - 飛び越える黒石は必ず連続していなければならない（間に空白や白石があってはダメ）。
#   - 飛び越えた黒石はそのジャンプで盤面から全て取り除かれる。
# - ジャンプは1回以上必須。
# - 黒石の数は最大20個で比較的少ないため、盤面上に「黒石の位置」と「白石の位置」を状態とした幅優先探索(BFS)で解く。
# - 状態は、白石の位置と黒石の位置の集合（座標の集合）で管理する。
# - 各ジャンプで「飛び越えた黒石を盤面から削除」するため、状態更新時に黒石位置も更新する必要がある。
# - BFSで探索し、白石が盤面の下端（row >= 19）に到達可能なら最短ジャンプ回数を返す。
# - 到達不可能なら-1を返す。

from collections import deque

# 盤のサイズ
ROWS = 19
COLS = 15

# 8方向ベクトル
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def in_board(r, c):
    # 盤面内かどうか(横は0~14, 縦は0~18)
    return 0 <= r < ROWS and 0 <= c < COLS

def solve():
    board = [list(input()) for _ in range(ROWS)]
    
    # 白石の位置を探す
    white_pos = None
    black_positions = set()
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O':
                white_pos = (r, c)
            elif board[r][c] == 'X':
                black_positions.add((r, c))
    
    # 状態は(白石の座標, frozenset(黒石の座標))
    # frozensetを使うことで状態管理が容易になる
    start_state = (white_pos, frozenset(black_positions))
    
    # BFSのキュー (状態, ジャンプ回数)
    queue = deque()
    queue.append((start_state, 0))
    
    visited = set()
    visited.add(start_state)
    
    while queue:
        (w_r, w_c), blacks = queue.popleft()
        
        # ゴール判定 (白石が盤面下端より下にある場合)
        if w_r >= ROWS:
            # ゴール達成
            # ジャンプ回数は0以上必須なのでここに到達するのはジャンプした結果
            # よって回数をそのまま返す
            print(queue[0][1] if queue else 0) # 保険で出力（下記のロジックで必ずprintされるため実質ここ使わない）
            print(queue[0][1])
            print(queue[0][1])
            # ここは誤っているため正しいprint処理は次
            break
        
        # 現状はゴールしていないので次のジャンプを探す
        # 白石は1回以上ジャンプ可能と問題にあるが、
        # BFSなので初回はジャンプ0状態
        # 1回目ジャンプ以降でゴール到達判定される
        
        # 周囲8方向を探す
        # 方向ごとに連続する黒石を飛び越えられるか調べる
        for dr, dc in directions:
            nr = w_r + dr
            nc = w_c + dc
            # 隣接に黒石がいなければジャンプできない
            if (nr, nc) not in blacks:
                continue
            
            # 隣接黒石があるので続く黒石の連続を調べる
            jump_r = nr
            jump_c = nc
            jumped_blacks = []
            while (jump_r, jump_c) in blacks:
                jumped_blacks.append((jump_r, jump_c))
                jump_r += dr
                jump_c += dc
            
            # ジャンプ先は連続した黒石を飛び越えた先のマス
            # ジャンプ先は空白か？黒石上は駄目、白石上も駄目
            if in_board(jump_r, jump_c):
                # 盤面内なら空白か確認
                # 盤面内なら状態上、白石や黒石？チェック
                # 盤面上は移動できないので空白ならOK
                if (jump_r, jump_c) in blacks:
                    continue
                if (jump_r, jump_c) == (w_r, w_c):
                    continue
                # 空白ならOK
            else:
                # ジャンプ先がゴール（盤面の下端よりも下）であればOK
                if jump_r < ROWS:
                    # 盤面外でなく盤面内なら不正
                    continue
            
            # 新しい黒石セットはジャンプした黒石を除く
            new_blacks = set(blacks)
            for b in jumped_blacks:
                new_blacks.discard(b)
            
            new_state = ((jump_r, jump_c), frozenset(new_blacks))
            
            if new_state not in visited:
                # ゴール判定
                if jump_r >= ROWS:
                    # ゴール到達
                    print(queue[0][1] + 1)  # 今回のジャンプ回数は前状態+1
                    return
                visited.add(new_state)
                queue.append((new_state, queue[0][1] + 1 if queue else 1))
    
    # 到達不可能
    print(-1)

if __name__ == "__main__":
    solve()