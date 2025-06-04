from collections import deque

# 座標の対応付けと隣接関係を定義する
# 11パズルの形状（図1の配置）をもとに全13マスの位置を固定で扱う
# 各行のマスの数は [1,3,5,3,1]
# マス番号を0から12とし、p1-p13に対応
# 入力行ごとの位置は以下の通り(インデックスは0始まり)
# row 0: [0]
# row 1: [1,2,3]
# row 2: [4,5,6,7,8]
# row 3: [9,10,11]
# row 4: [12]

# 0~12までの各マスとそこに隣接するマスのインデックス一覧
neighbors = {
    0: [1],
    1: [0,2,4],
    2: [1,3,5],
    3: [2,6],
    4: [1,5,9],
    5: [2,4,6,10],
    6: [3,5,7,11],
    7: [6,8,12],
    8: [7],
    9: [4,10],
    10: [5,9,11],
    11: [6,10,12],
    12: [7,11],
}

# 完成形（ゴール）を定義
# 以下は問題文の図2完成型にあわせる。
# 問題文の完成型が明示されていないため、0が2つの空きで数字が1から11の順になると推定
# 13マスのうち空白は2つ、数字は1~11のカード
# ゴールは左上から右下に向けて
# 空白は12,7マスが空き（図2のパターンを想定として）
# 以下は一例。もし問題と違ったら調整が必要。
# 1行目:1
# 2行目:2 3 4
# 3行目:5 6 7 8 9
# 4行目:10 11 0
# 5行目:0
# よってインデックスに対応させると
goal_state = (
    1,
    2,3,4,
    5,6,7,8,9,
    10,11,0,
    0,
)

# 入力は13行それぞれの行からマスを読む
# 各行のマスの数は [1,3,5,3,1]
# 入力位置をstateの0~12に対応させる必要がある

# 行毎のマス数
line_cells_counts = [1,3,5,3,1]
# 入力13行に対して行ごとにマスをどのインデックスに展開するか
# 入力の13行目まであるのはパズルの形により一行にまとめられないためか？
# 実際は13行読み込んで展開する。行ごとの分割は以下の通り
# 入力行ごとのセル数（1個または複数個）が問題文例より読み取れる。
# サンプル入力の１データ例から見ると、13行あるのは、各行に複数セルが分散されている可能性が高い。
# 実際、問題の例では行数13に分割されている。
# 具体的には
# 6
# 2 1 3
# 10 5 7 0 8
# 9 4 11
# 0
# 2行目は 2 1 3 (3個)
# 3行目は 10 5 7 0 8 (5個)
# 4行目は 9 4 11 (3個)
# それ以外は1個ずつの行がある
# よって13行目まであるが、実際は13マスの集合ではなく、このような形か？
# 実はp1～p13とあり、13行入力がある。13個のスロットに順番に数字が入る。
# そのまま、0から12までインデックスに対応する。

# よってシンプルに13行入力を0-12の位置にマップ

def read_state(lines):
    # linesは13行のリスト（文字列で数字）
    state = tuple(int(x) for x in lines)
    return state

def find_zero_positions(state):
    # 空きスペース＝数字０の場所、2つあるはず
    return [i for i,v in enumerate(state) if v == 0]

def is_goal(state):
    return state == goal_state

def serialize_state(state):
    # tuple 状態のままでOK
    return state

def can_move(zs, pos):
    # 空白のどちらかに隣接していて動かせるマスかどうか
    return any(pos in neighbors[z] for z in zs)

def move(state, zero_positions, card_pos):
    # card_posのカードを空白1つ分動かし、空白スペースと入れ替える
    # ただし、空白が2つあるためどちらと入れ替えればよいか？
    # 同じ空白に隣接でなければ動けないことを確認済み

    # どちらの空白に隣接か判定して近い空白を入れ替え
    z1,z2 = zero_positions
    if card_pos in neighbors[z1]:
        # z1と入れ替え
        lst = list(state)
        lst[z1], lst[card_pos] = lst[card_pos], lst[z1]
        return tuple(lst)
    elif card_pos in neighbors[z2]:
        # z2と入れ替え
        lst = list(state)
        lst[z2], lst[card_pos] = lst[card_pos], lst[z2]
        return tuple(lst)
    else:
        # 隣接しない
        return None

def solve_11_puzzle(initial_state):
    if is_goal(initial_state):
        return 0
    visited = set()
    visited.add(initial_state)
    q = deque()
    # queue要素は：(state, cost)
    q.append((initial_state,0))

    while q:
        state, cost = q.popleft()
        if cost > 20:
            return "NA"
        zero_positions = find_zero_positions(state)
        # 空白2つに隣接するカードの位置を探す
        movable_positions = set()
        for z in zero_positions:
            movable_positions.update(neighbors[z])
        for pos in movable_positions:
            new_state = move(state, zero_positions, pos)
            if new_state is None:
                continue
            if new_state == goal_state:
                return cost + 1
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, cost+1))
    return "NA"

def main():
    import sys
    lines = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line=line.strip()
        if line == '-1':
            break
        lines.append(line)
    # 一つのデータセットは13行
    # 複数セットあるので13行ずつ処理
    for i in range(0,len(lines),13):
        data = lines[i:i+13]
        if len(data)<13:
            break
        state = read_state(data)
        ans = solve_11_puzzle(state)
        print(ans)

if __name__ == '__main__':
    main()