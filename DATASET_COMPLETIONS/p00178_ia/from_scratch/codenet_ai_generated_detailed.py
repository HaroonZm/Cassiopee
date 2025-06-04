# テトリス風ゲームの実装
# 入力として複数のデータセットを読み込み、それぞれの最後に残るブロックの総個数を出力する。

# アプローチ：
# 盤面幅は5で固定。高さは十分。
# ブロックを落とすたびに、ブロックの位置と形状を考慮して落ちる高さ（y座標）を決定する。
# 横向きブロックの場合：
#   ブロックの幅＝p_i、位置＝q_i（左端から1~5）
#   盤面の指定位置の列群の最高位置を見て、その上に置く。
# 縦向きブロックの場合：
#   縦に連なったp_i個を1列に落とす。場所はq_i列目。
# ブロックを置いた後、横一行（5列全部が埋まった行）があれば消す。
# 消えた行の上の部分は一行ずつ落ちる。
# この処理をn回繰り返す。
# 最後に盤面に残っているブロック（Trueなマス）の個数を数える。

# 盤面はリストのリストで保持。board[y][x] = bool（Trueならブロック有り）
# y=0が下の行。

def tetris_game():
    import sys
    input = sys.stdin.readline
    
    while True:
        n_line = input()
        if not n_line:
            break
        n = n_line.strip()
        if n == '0':
            break
        n = int(n)
        
        # 盤面を初期化（高さ1000で十分）
        # y=0が下端
        max_height = 1000
        width = 5
        board = [[False]*width for _ in range(max_height)]
        
        # 現状の最高の高さ(1行でもブロックあればその行番号+1)
        current_highest = 0
        
        for _ in range(n):
            d,p,q = input().split()
            d = int(d)
            p = int(p)
            q = int(q) - 1  # 0-indexedへ
            
            # 落ちる位置を決定
            # 横向きのブロック：幅p、位置q（左端）
            # 縦向きのブロック：長さp、高さ方向に。
            
            # 落ちる高さを探す
            if d == 1:
                # 横向きブロック
                # qからq+p-1までが範囲
                # 各列の最高ブロックの高さを調べて、そこからブロックが落ちる高さを決定
                # 各列で最新の積み上げ高さを調べる
                max_col_height = -1
                for col in range(q, q+p):
                    # 0から現在最高までの高さでブロックあるかチェック
                    col_height = -1
                    for h in range(current_highest):
                        if board[h][col]:
                            col_height = h
                    max_col_height = max(max_col_height, col_height)
                # 落ちる高さは max_col_height + 1
                drop_height = max_col_height + 1
                # ブロックを置く高さがboardの高さ内かチェック
                if drop_height + 0 >= max_height:
                    raise RuntimeError("Board height overflow")
                # ブロックを置く
                for col in range(q, q+p):
                    board[drop_height][col] = True
                
                if drop_height + 1 > current_highest:
                    current_highest = drop_height + 1
                
            else:
                # 縦向きブロック
                # q列目にp個連続
                # 各列の最高ブロックの高さは列qの最高を探す
                col = q
                col_height = -1
                for h in range(current_highest):
                    if board[h][col]:
                        col_height = h
                # 縦長のブロックが置ける高さはcol_height + 1という底の位置に置くと、
                # 一番下がcol_height+1
                drop_bottom = col_height + 1
                # でもブロックの上端は drop_bottom + p -1
                # 紛らわしいが落ちる位置は底の高さ
                
                # ここで垂直方向に綺麗に積むために、p個縦に並べて置く
                top_pos = drop_bottom + p - 1
                if top_pos >= max_height:
                    raise RuntimeError("Board height overflow")

                for dy in range(p):
                    board[drop_bottom + dy][col] = True
                
                if top_pos + 1 > current_highest:
                    current_highest = top_pos + 1
                
            # 横一行が全て埋まっている場合は消す処理
            # boardの0からcurrent_highest-1まで走査
            # 消える行があれば消す
            # 消したら上のブロックを下げる
            # 複数行消えることもあるので繰り返す
            while True:
                row_to_remove = -1
                for row_i in range(current_highest):
                    if all(board[row_i][col] for col in range(width)):
                        row_to_remove = row_i
                        break
                if row_to_remove == -1:
                    break  # 消す行が無い
                
                # 行を消す（その行を削除して上の行を1下げる）
                for row_idx in range(row_to_remove, current_highest-1):
                    board[row_idx] = board[row_idx+1][:]
                # 最上段は空にする
                board[current_highest-1] = [False]*width
                current_highest -= 1
                if current_highest < 0:
                    current_highest = 0
        
        # 最後に残るブロックの個数を数える
        ans = 0
        for y in range(current_highest):
            for x in range(width):
                if board[y][x]:
                    ans += 1
        print(ans)

if __name__ == "__main__":
    tetris_game()