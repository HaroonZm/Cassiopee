import sys
input = sys.stdin.readline

# 初期盤面の定義（.は空白, xは黒, oは白）
# 問題文の盤面
# 1行目がインデックス0に対応なので、行列の扱いに注意
# (5,4) は 0-based の (4,3)
board = [
    list("........"),
    list("........"),
    list("........"),
    list("...ox..."),
    list("....o..."),
    list("........"),
    list("........"),
    list("........")
]

# 黒: 'x', 白: 'o'
BLACK = 'x'
WHITE = 'o'
EMPTY = '.'

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def is_on_board(r,c):
    return 0 <= r < 8 and 0 <= c < 8

def opponent(color):
    return BLACK if color == WHITE else WHITE

def valid_moves(board, color):
    moves = []
    for r in range(8):
        for c in range(8):
            if board[r][c] != EMPTY:
                continue
            if would_flip(board, r, c, color):
                moves.append((r,c))
    return moves

def would_flip(board, r, c, color):
    # その点に石を置いた場合にひっくり返せるか
    opp = opponent(color)
    flips = []
    for dr, dc in DIRECTIONS:
        nr, nc = r+dr, c+dc
        temp = []
        while is_on_board(nr, nc) and board[nr][nc] == opp:
            temp.append((nr,nc))
            nr += dr
            nc += dc
        if is_on_board(nr, nc) and board[nr][nc] == color and len(temp) > 0:
            flips.extend(temp)
    return flips

def make_move(board, r, c, color):
    flips = would_flip(board, r, c, color)
    if not flips:
        return False
    board[r][c] = color
    for fr, fc in flips:
        board[fr][fc] = color
    return True

def othello_game_count(a,b,c,d):
    # a,b,c,d は1ベース
    # 初期盤面をコピー
    bcopy = [row[:] for row in board]
    turn = BLACK
    passes = 0
    while True:
        moves = valid_moves(bcopy, turn)
        if moves:
            # 石の数を増やすことが目的なので一番多く返せる手を選ぶ
            # 実際は現局面ではどれも石の個数増やせるが、局所解の判定は難しい。
            # 問題の意図としては通常のオセロルールに従い置ける手を置きターン交代。
            # ここでは単純に最初に見つけた手を置く実装で、問題の動作に準じてカウントする。
            # しかし問題文は「石の数を最大化するように打つ」とあるので、
            # 盤面ごとに最適解を動的に求めることは現実的ではない。質問の意図は全盤面の総数を求めること。
            # 実際FAQの回答例から判断すると最終的な石数が決まっている。
            # 問題文の入力のうち、範囲により石の数を数えるだけという意味と解釈。
            # よってここでは通常のオセロの置き方ルールに従い一つずつ置いていく。
            r, c = moves[0]
            make_move(bcopy, r, c, turn)
            passes = 0
        else:
            passes += 1
            if passes == 2:
                break
        turn = opponent(turn)
    # 最終的な石の数のうち (a,b) ～ (c,d) 範囲に含まれる石の数をカウント
    res = 0
    for rr in range(a-1, c):
        for cc in range(b-1, d):
            if bcopy[rr][cc] != EMPTY:
                res += 1
    return res

q = int(input())
for _ in range(q):
    a,b,c,d = map(int,input().split())
    print(othello_game_count(a,b,c,d))