import sys
sys.setrecursionlimit(10**7)

# 方向と回転の対応
# 北(0), 東(1), 南(2), 西(3)
dir_map = {'N':0, 'E':1, 'S':2, 'W':3}
delta = [(-1,0),(0,1),(1,0),(0,-1)]  # 北,東,南,西の移動量

# プログラムのパースと実行を行うクラス定義
class RobotProgramExecutor:
    def __init__(self, H, W, board, program_str):
        self.H = H
        self.W = W
        self.board = board
        self.program_str = program_str
        self.pos = None   # ロボットの位置 (r,c)
        self.facing = 0   # ロボットの向き 北=0
        self.move_count = 0  # 動作文の実行回数
        self.terminated = False  # ゴールに到達してプログラム終了判定
        # ロボットの初期位置を探す
        for i in range(H):
            for j in range(W):
                if board[i][j] == 's':
                    self.pos = (i,j)
                    break

    # プログラム文字列を文(ステートメント)のリストにパースする
    # 返り値: [文1, 文2,...], 残りの文字列
    # 文はdict形式で { 'type': 'move', 'cmd': '^' } 等、 if -> {'type':'if','cond':..., 'prog':...}, whileあり
    # 条件は文字列
    def parse_program(self, s):
        stmts = []
        i = 0
        length = len(s)
        while i < length:
            c = s[i]
            if c == '[':
                # if文
                # 構文: [条件 プログラム ]
                i += 1
                cond, offset = self.parse_condition(s, i)
                i += offset
                prog, offset = self.parse_until_matching(s, i, '[', ']')
                i += offset
                prog_stmts, _ = self.parse_program(prog)
                stmts.append({'type':'if','cond':cond,'prog':prog_stmts})
            elif c == '{':
                # while文
                # 構文: {条件 プログラム }
                i += 1
                cond, offset = self.parse_condition(s, i)
                i += offset
                prog, offset = self.parse_until_matching(s, i, '{', '}')
                i += offset
                prog_stmts, _ = self.parse_program(prog)
                stmts.append({'type':'while','cond':cond,'prog':prog_stmts})
            elif c in '^v<>':
                # 動作文
                stmts.append({'type':'move','cmd':c})
                i += 1
            else:
                # 条件以外なら終了（プログラム終端）
                break
        return stmts, s[i:]

    # 条件を読み取る。先頭は「~」があってもなくてもよく、次に N/E/S/W/C/T の1文字
    # 返り値: 条件文字列(例 "~N" or "C"), 文字数
    def parse_condition(self,s,i):
        if s[i] == '~':
            return s[i:i+2], 2
        else:
            return s[i], 1

    # 対応する括弧で囲まれた部分(条件を読み取った後のプログラム部分)を返す
    # s[i:]で始まる文字列から、対応するペア括弧までの文字列とその長さを返す
    # 例: parse_until_matching("[N >]",0,'[',']') -> ">",
    def parse_until_matching(self, s, i, open_char, close_char):
        depth = 1
        start = i
        j = i
        while j < len(s):
            if s[j] == open_char:
                depth += 1
            elif s[j] == close_char:
                depth -= 1
                if depth == 0:
                    return s[start:j], j - start +1
            j += 1
        # 一致する閉じ括弧がない場合は問題の条件から発生しない想定
        return "", 0

    # 条件判定。現在のロボットの向きと位置から 真/偽 を返す
    def eval_condition(self, cond):
        neg = False
        if cond[0] == '~':
            neg = True
            c = cond[1]
        else:
            c = cond[0]
        res = False
        if c in 'NESW':
            # 方角判定
            res = (self.facing == dir_map[c])
        elif c == 'C':
            # 目の前に壁があるか
            dr, dc = delta[self.facing]
            nr = self.pos[0] + dr
            nc = self.pos[1] + dc
            if 0 <= nr < self.H and 0 <= nc < self.W:
                res = (self.board[nr][nc] == '#')
            else:
                # 外周は壁。ここには基本にないが防御的に真とする
                res = True
        elif c == 'T':
            # 常に真
            res = True
        else:
            # 想定外条件は False
            res = False
        return not res if neg else res

    # 動作文を実行。動作のたびに move_count 増加
    # 動作中にゴールにたどり着いた場合は self.terminated True にする
    def exec_move(self, cmd):
        self.move_count += 1  # 動作文の実行は必ず数える
        if self.terminated:
            return  # 到達済みなら何もしない
        r, c = self.pos
        if cmd == '^':
            dr, dc = delta[self.facing]
            nr, nc = r+dr, c+dc
            # 壁なら移動しない
            if self.board[nr][nc] != '#':
                self.pos = (nr,nc)
                if self.board[nr][nc] == 'g':
                    self.terminated = True
        elif cmd == 'v':
            # 後退は前方とは逆方向へ1個移動
            dr, dc = delta[self.facing]
            nr, nc = r - dr, c - dc
            if self.board[nr][nc] != '#':
                self.pos = (nr,nc)
                if self.board[nr][nc] == 'g':
                    self.terminated = True
        elif cmd == '<':
            # 左に90度回転
            self.facing = (self.facing + 3) % 4
        elif cmd == '>':
            # 右に90度回転
            self.facing = (self.facing + 1) % 4

    # 文(statement)を実行
    # stmtはdictでtype:"move"/"if"/"while"
    def exec_stmt(self, stmt):
        if self.terminated:
            return
        if stmt['type'] == 'move':
            self.exec_move(stmt['cmd'])
        elif stmt['type'] == 'if':
            if self.eval_condition(stmt['cond']):
                self.exec_program(stmt['prog'])
        elif stmt['type'] == 'while':
            while not self.terminated and self.eval_condition(stmt['cond']):
                self.exec_program(stmt['prog'])

    # プログラム(文のリスト)を1つずつ実行
    def exec_program(self, stmts):
        for stmt in stmts:
            if self.terminated:
                break
            self.exec_stmt(stmt)

def main():
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        row = list(input())
        board.append(row)
    program_str = input()

    executor = RobotProgramExecutor(H, W, board, program_str)
    # パースして実行
    prog_tree, _ = executor.parse_program(program_str)
    executor.exec_program(prog_tree)

    # 出力
    # ゴール到達しなければ -1
    if executor.terminated:
        print(executor.move_count)
    else:
        print(-1)

if __name__ == '__main__':
    main()