# 解説：
# - 初期状態は全マス白('o')。
# - 操作は、上から偶数番目かつ左から偶数番目の白マスを選び、そのマスとそのマスの上下左右方向に連鎖的に白マスがなくなるまで黒マス('x')に変える。
# - ゴールは与えられたマス状態にすること。最低操作回数を求める。
#
# 重要なポイント：
# - 操作を適用できるのは、(偶数行、偶数列)の白マスのみ。
#   ここでインデックスは1始まりとし、0-basedでは(奇数,奇数)となる。
# - 操作が加える黒マスの変化はこの規則的で、しかも
#   操作は足し合わせてビット演算的に考えられることが多い。
# - 問題の制約と解法としては、XOR（排他的論理和）を利用した
#   連立一次方程式の解法で典型的な「滴模式問題」と考えられる。
#
# アプローチ：
# - グリッドの各マスを変数の集合と見て、操作は変数の線形結合として表す。
# - 操作できるセルは M = ((N-1)//2)^2 個程度。
# - 操作による影響はどのマスに作用するかを表現した行列を構築。
# - 各マスの最終状態を0（白）か1（黒）としてビットベクトルを作る。
# - この連立一次方程式をガウス・ジョルダン法で解き、最少の操作数を得る。
#
# 実装詳細：
# - 入力は N (奇数) と状態の文字列。
# - インデックスは0始まりで扱う。
# - 操作可能な座標は i,j がともに奇数（0-basedで）のマス。
# - それぞれの操作の効果は、
#   選んだマスは黒、上下方向の連続白マスは黒、左右方向も同様。
# - 操作行列を構築し、対象マスの最終状態ベクトルを作成。
# - 連立方程式 Ax = b を解く（すべて mod 2）。
# - 解で、x の1の数（操作回数）を最小化する。
#
# 参考：
# - 127は許容可能な行列サイズ（最大約64^2=4096の変数と対象）
# - 最悪でもビット演算を駆使して高速実装可能。

import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = [list(input().rstrip()) for _ in range(N)]
    
    # メモ：
    # 操作可能なセルの数を求める
    # (奇数0-based)のi,j かつ白のセルだけ検討するため、リスト化
    
    ops = []
    # 0-based 偶数番目 -> i,jは奇数（1始まりで偶数）
    # 例えば、N=5の時、有効位置は (1,1), (1,3), (3,1), (3,3)
    for i in range(1,N,2):
        for j in range(1,N,2):
            if A[i][j] == 'o':
                ops.append((i,j))
    
    # 行列の行数はN*N（すべてのマスの状態を表す）
    # 列数はlen(ops)（操作変数の数）
    # 行列AはN*N x len(ops)
    size_row = N*N
    size_col = len(ops)
    
    # 行列、ベクトル作成
    # A[row][col] = 操作 col がマス row にどう影響するか
    # マスの番号は i*N + j
    A_mat = [0]*(size_row)  # 各行をビット列で表す（列はbitで表しきれないので整数リストに変換）
    # Pythonはビット長制限無しintなので、bitシフトで表現可能
    # size_col 最大約 ((N+1)//2)^2 127なら最大64^2=4096くらい
    # これは1つのintでは扱いきれないので、ビット配列やリストで管理する必要あり。
    #
    # ここでは長いビットベクトルを[整数ブロック]で持つ方式を採用
    # 1整数は64bit扱えるとして、64bitごとに分割
    
    from math import ceil
    BLOCK_SIZE = 64
    BLOCK_NUM = ceil(size_col / BLOCK_SIZE)
    
    # A_matは行ごとにブロック数のlistで管理
    A_mat = [[0]*BLOCK_NUM for _ in range(size_row)]
    
    # bベクトル：最終の黒マスを1に
    b_vec = [0]*size_row
    
    # フィル (A_mat, b_vec)の構成
    # 操作の効果を計算する関数
    # 操作位置(i,j)を選ぶと、(i,j)がxになる
    # その上下に連鎖している白を黒に変える
    #　左右も同様
    
    # 操作効果ベクトルを作り、それを行列列としてセット
    # i,jは操作座標
    def effect_cells(i,j):
        cells = []
        idx = i*N + j
        cells.append(idx)
        # 上方向
        r = i-1
        while r >= 0 and A[r][j] == 'o':
            cells.append(r*N + j)
            r -= 1
        # 下方向
        r = i+1
        while r < N and A[r][j] == 'o':
            cells.append(r*N + j)
            r += 1
        # 左方向
        c = j-1
        while c >= 0 and A[i][c] == 'o':
            cells.append(i*N + c)
            c -= 1
        # 右方向
        c = j+1
        while c < N and A[i][c] == 'o':
            cells.append(i*N + c)
            c += 1
        return cells
    
    # A_matの列を設定
    # ops の順に列idxを与える
    for col, (i,j) in enumerate(ops):
        cells = effect_cells(i,j)
        block_id = col // BLOCK_SIZE
        bit_id = col % BLOCK_SIZE
        mask = 1 << bit_id
        for pos in cells:
            A_mat[pos][block_id] ^= mask
    
    # b_vecの設定：最終状態が黒('x')なら1, 白('o')なら0
    for i in range(N):
        for j in range(N):
            idx = i*N + j
            b_vec[idx] = 1 if A[i][j] == 'x' else 0
    
    # ガウス・ジョルダン消去を行う関数
    # 行列をbitブロックで処理する：行優先でpivotを探し、行交換、排除を繰り返す
    def gauss_jordan(A_mat, b_vec):
        rank = 0
        n = len(A_mat)  # 行数=N*N
        m = size_col     # 列数=len(ops)
        
        for col in range(m):
            block_id = col // BLOCK_SIZE
            bit_id = col % BLOCK_SIZE
            mask = 1 << bit_id
            
            pivot = -1
            for row in range(rank, n):
                if (A_mat[row][block_id] & mask) != 0:
                    pivot = row
                    break
            
            if pivot == -1:
                # この列は全部0 => 次の列へ
                continue
            
            # pivot行とrank行を交換
            if pivot != rank:
                A_mat[pivot], A_mat[rank] = A_mat[rank], A_mat[pivot]
                b_vec[pivot], b_vec[rank] = b_vec[rank], b_vec[pivot]
            
            # pivot行で他行のcol bitを消去
            for row in range(n):
                if row != rank and (A_mat[row][block_id] & mask) != 0:
                    # A_mat[row] ^= A_mat[rank]
                    for b in range(BLOCK_NUM):
                        A_mat[row][b] ^= A_mat[rank][b]
                    b_vec[row] ^= b_vec[rank]
            
            rank += 1
        
        # 解の存在チェックは問題文では必ず存在するとあるので省略
        
        # 解の復元
        # 基本解は0で、pivot位置がわかる
        x_vec = [0]*m
        
        # pivot位置を探して解を決定（後退代入はpivot昇順で通用）
        # pivot列の場所は各行で1つだけあるはず（行の中のleftmost 1）
        # ただし今回のガウス・ジョルダンは完全消去済なので、
        # x_colをpivotに割り当てているので左から行って求められる。
        # ここでreduced row echelon formなので、1つだけ1がある列がpivot列。
        
        # pivot列→行対応を作る
        pivot_pos = [-1]*m  # pivot_pos[col] = row where col pivot
        # 行ごとのpivot列を探す
        for row in range(rank):
            # leftmost 1 bitを探す
            for b in range(BLOCK_NUM):
                val = A_mat[row][b]
                if val != 0:
                    # 最左のbitを探す
                    for bit in range(BLOCK_SIZE):
                        if (val >> bit) & 1:
                            pivot_col = b*BLOCK_SIZE + bit
                            if pivot_col < m:
                                pivot_pos[pivot_col] = row
                            break
                    break
        
        # 復元
        # 解は b_vec[row] と対応pivot列のxに代入される
        for col in range(m-1,-1,-1):
            row = pivot_pos[col]
            if row == -1:
                # free variable → 0とする（最小化狙い）
                x_vec[col] = 0
                continue
            val = b_vec[row]
            # pivot以外のcolに注目しない（RREFだから1つのピボットしか1無し）
            x_vec[col] = val
        
        return x_vec
    
    x_sol = gauss_jordan(A_mat, b_vec)
    
    # x_solの1の数が答え（最小操作回数）
    ans = sum(x_sol)
    print(ans)

if __name__=="__main__":
    main()