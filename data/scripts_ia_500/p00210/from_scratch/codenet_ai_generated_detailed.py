# 解説：
# 問題は、W×H の迷路内で複数の人が同時に避難行動を行うシミュレーションです。
# 人は向いている方向に基づき、右→前→左→後 のマス目を順に見て最初に通路か非常口があれば向きを変える。
# その後、前が空いていて他の人と衝突しなければ移動。
# 複数人が同じマスに移動しようとしている場合、東→北→西→南 の順で人を選択して一人だけ移動。
# 移動後に非常口に到達した人は迷路から消えます。
# 全員が脱出するまでの時間を計測、180秒越えたらNA。

# 解法のポイント
# - 人の状態を(x,y,方向)で管理
# - 毎秒、人全員同時に方向転換と移動判定を行い、移動候補を収集
# - 移動候補の衝突はルールに従って解決
# - 移動更新後、非常口到達者を削除
# - 180秒まで繰り返し、終了か判定
# - 複数データセット処理

# 方向情報
# 方向は 'E','N','W','S' 4方向。dx,dyを定める。
# 右、前、左、後 は現在方向からの相対的な変化として表現。

import sys

# 東、北、西、南の順に (x,y) 増減
DIRS = {
    'E': (1, 0),
    'N': (0, -1),
    'W': (-1, 0),
    'S': (0, 1),
}

# 方向の順番 (東,北,西,南)
ORDER_DIR = ['E', 'N', 'W', 'S']

# 右、前、左、後の方向変化を index 0=現在の向き
# インデックスは RIGHT=0, FRONT=1, LEFT=2, BACK=3 の順になっている
# ここで定義するのは、今向いてる方向を0として
# 右は90度時計回り、前は0度、左は90度反時計回り、後は180度反転
# → 方角リスト ORDER_DIR で角度を管理し、現在方角のインデックスから (+1)%4, 0, (+3)%4, (+2)%4 に対応。
TURN_OFFSETS = [1, 0, 3, 2]  # right, front, left, back のインデックス差

def turn_dir(current_dir, turn_idx):
    # 現在の方向からTURN_OFFSETSを足した方向
    cur_idx = ORDER_DIR.index(current_dir)
    return ORDER_DIR[(cur_idx + TURN_OFFSETS[turn_idx]) % 4]

def simulate(W, H, grid):
    people = []
    exits = set()
    
    # 人の初期位置と向きを取得
    # 非常口も記録
    for y in range(H):
        for x in range(W):
            c = grid[y][x]
            if c in ['E','N','W','S']:
                people.append( [x, y, c] )
                # 床に置き換える（人のマークは床扱い）
                grid[y] = grid[y][:x] + '.' + grid[y][x+1:]
            elif c == 'X':
                exits.add( (x,y) )
    # 180秒制限
    MAX_TIME = 180
    
    # 1秒ごとに以下の処理を行う
    # - 各人は、右、前、左、後の順に隣接セルを確認し、
    #   最初に通路または非常口があればそちらに向きを変える。
    #   なければ向きを変えない。
    # - 移動可能かチェック（目の前が通路か非常口、且つ他の人が狙っていない）
    # - 移動候補が被る場合、東→北→西→南の順に優先して一名だけ移動
    # - 移動後、非常口にいれば脱出(消す)
    
    for t in range(1, MAX_TIME+1):
        # 方向変更フェーズ
        new_dirs = []
        for px, py, pd in people:
            # 右、前、左、後の4方向を順に確認
            turned = pd
            moved_dir = None
            for turn_i in range(4):
                d = turn_dir(pd, turn_i)
                dx, dy = DIRS[d]
                nx, ny = px + dx, py + dy
                if 0 <= nx < W and 0 <= ny < H:
                    c = grid[ny][nx]
                    if c == '.' or c == 'X': # 通路または非常口
                        moved_dir = d
                        break
            if moved_dir is not None:
                new_dirs.append(moved_dir)
            else:
                new_dirs.append(pd)
        # 移動判定フェーズ
        # 各人の前方マスを計算
        front_cells = []
        # マスごとの前方にいる人(インデックス)リストを作成
        cell_to_people = dict()
        for i, (p, d) in enumerate(zip(people, new_dirs)):
            x, y = p[0], p[1]
            dx, dy = DIRS[d]
            nx, ny = x+dx, y+dy
            front_cells.append( (nx, ny) )
            cell_to_people.setdefault( (nx, ny), [] ).append(i)
        # 移動希望リスト（i番の人が移動可能か）
        can_move = [False]*len(people)
        # 衝突判定
        # 以下の条件を満たすマスは移動可:
        # - 床か非常口
        # - そのマスに複数人が移動したい場合、東→北→西→南 の順で優先
        # なので、各マスで複数人が居た場合、人の向き順で優先順位付け
        for cell, indices in cell_to_people.items():
            nx, ny = cell
            if 0 <= nx < W and 0 <= ny < H:
                c = grid[ny][nx]
                if c == '.' or c == 'X':
                    # indices は複数人の移動希望
                    if len(indices) == 1:
                        # 問題文：他人の目の前のマスになっていない → この集合は目の前のマス複数人分の集合だから、
                        # 複数重複は無視で良い。ひとりだけならば衝突なし。
                        can_move[indices[0]] = True
                    else:
                        # 複数人いる場合、東→北→西→南 の順で移動できる人を1人だけ選ぶ
                        # 複数人が同じマスに向かう場合の優先順位判定：
                        # それぞれの人の向きを取得し、ORDER_DIRで先にある方を優先
                        
                        # indices から移動可能な人候補をソート
                        sorted_indices = sorted(indices, key=lambda idx: ORDER_DIR.index(new_dirs[idx]))
                        # 一人だけ移動可能を許可
                        can_move[sorted_indices[0]] = True
        # 移動実行
        new_people = []
        for i, (pos, d) in enumerate(zip(people, new_dirs)):
            if can_move[i]:
                nx, ny = front_cells[i]
                # 移動後に非常口なら脱出
                if (nx, ny) in exits:
                    # 脱出者は記録しない
                    continue
                else:
                    new_people.append([nx, ny, d])
            else:
                # 移動しない場合は現在位置、変更後方向で更新
                new_people.append([pos[0], pos[1], d])
        people = new_people
        # 全員脱出したら終了
        if not people:
            return t
    # 180秒超えたらNA
    return "NA"

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if not line:
            continue
        W_H = line.split()
        if len(W_H) != 2:
            continue
        W, H = map(int, W_H)
        if W == 0 and H == 0:
            break
        grid = []
        for _ in range(H):
            grid.append(input_lines[idx])
            idx += 1
        ans = simulate(W, H, grid)
        print(ans)

if __name__ == "__main__":
    main()