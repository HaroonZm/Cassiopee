import sys
from collections import deque

# 問題の条件を整理すると、3つのトレイ（A,B,C）に大小異なるn個のコップが積まれている状態を表現し、
# 移動可能な操作は
#   - 一度に一つのコップを移動
#   - 移動できるのは各トレイの一番上（最も大きいコップ）
#   - 大きいコップの上に小さいコップは置けない（常に昇順に積まれている）
#   - 直接移動はA<->B、B<->C間のみ可能で、A<->C間は不可
# とある。
# これを満たしつつ、m回以内で全てのコップをAかCのトレイのどちらかにまとめる最小手数を求め、
# 不可能な場合-1を出力する。

# 状態表現：
# 各コップ1..nに対し、どのトレイ(A:0, B:1, C:2)にあるかを配列やビットで定義する。
# n 最大15なので、1コップあたり2bitで3トレイを表現可能。
# よって全状態を30bitの整数（ビット操作）で表現可能。

# 探索：最短手数なので幅優先探索(BFS)で状態遷移を探索する。
# 訪問済み管理や遷移生成の高速化が必要。

# */
/*
状態bit配置例（2bit/コップ）：
コップiの位置は状態整数の下から2*i, 2*i+1ビット。
00=A, 01=B, 10=C。

例えば、n=3なら、
state = [p0,p1,p2]でp0=トレイID(0,1,2), p1=同様, p2=同様
をまとめて整数で保持。
*/

// 以下に詳細コメント付きで実装する。

def main():
    input = sys.stdin.readline

    # トレイ名定義
    A, B, C = 0,1,2
    # コップ位置を表す2bitの値でのマップ
    # トレイIDに対応：A=0, B=1, C=2

    # コップの位置stateは整数で保持:
    # コップiの位置は (state >> (2*i))&3
    # 3(0b11)は使わず0..2の値とする。

    # 位置をセットする関数
    def set_pos(state, idx, tray):
        # idx番目コップの位置をtrayにセットした新しいstateを返す
        # trayは0~2
        mask = 3 << (2*idx)
        return (state & ~mask) | (tray << (2*idx))

    # 位置を取得する関数
    def get_pos(state, idx):
        return (state >> (2*idx)) & 3

    # 引数で与えられたコップ配置の初期stateを作成
    # トレイリストは昇順で、index0が最小コップ、最後が最大コップ。
    # 最上は最後の要素(最大コップ)
    # 数が多いので、入力のコップをどの位置に置くかindexを整える。
    # 入力はトレイごとに昇順リスト(小さい順)なので、このまま使える。

    # BFSで状態遷移を作る際のポイント
    # - 現stateから移動可能なコップは各トレイ上に積まれている最大値（=上のコップ）
    # - もとのコップの集合(分割)から、3トレイの上のコップを判別するには、
    #   コップごとの位置情報とコップの大きさ(番号の大小)を使う
    # - そのため、各トレイの最大コップ（最大の番号を持つコップ）を特定できれば良い

    # 全トレイに積まれているコップ数や、上のコップは
    # それぞれのトレイのコップのうち最大番号のもの

    # そこで、大きいコップは必ず最上にいるので、コップの中で最大値のコップが上にいる。

    # よって、stateからトレイごとに積まれているコップ(集合)を取得し、
    # そこから最大値（番号）だけを取り出す

    # 移動可能なコップは最大コップ1個/トレイ

    # 探索は状態を整数で扱い、距離配列は辞書か配列
    # n最大15なので状態空間は3^15 ~ 1.4億（膨大）
    # mは最大1.5千万なので完全探索は厳しいが問題例から5個程度の入力で済む想定。
    # 状態はメモリ効率を考え、set()で管理

    # 訪問済み辞書：state -> 移動回数

    while True:
        line = input()
        if not line:
            break
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        # 3トレイ分の情報を受け取る
        # 各行は「個数 数列」で与えられる。
        # 昇順で並んでいる。
        # コップの番号は1..nで一意。
        tray_cups = []
        for _ in range(3):
            tokens = input().strip().split()
            cnt = int(tokens[0])
            if cnt > 0:
                cups = list(map(int, tokens[1:]))
            else:
                cups = []
            tray_cups.append(cups)

        # state構築:
        # 各コップ1..nの位置を決める
        # 初期は位置不定 ← すべてのコップに対応するため、-1で初期化し後でセット
        cup_pos = [-1]*(n+1)  # 1-indexed
        # tray_cups[i]は昇順だが小さいコップが一番下（下から順に大きくなる）
        # コップ位置はそのままトレイ番号で設定
        for tray_id in range(3):
            for c in tray_cups[tray_id]:
                cup_pos[c] = tray_id

        # 初期state作成
        state = 0
        for c in range(1, n+1):
            pos = cup_pos[c]
            state = set_pos(state, c-1, pos)

        # 目標判定関数
        # すべてのコップがAまたはCに集まっている状態
        # stateの全コップが0または全て2かどうか判定
        def is_goal(s):
            # すべてpos==0 or すべてpos==2
            pos0 = True
            pos2 = True
            for i in range(n):
                p = get_pos(s, i)
                if p != 0:
                    pos0 = False
                if p != 2:
                    pos2 = False
                if not pos0 and not pos2:
                    return False
            return True

        if is_goal(state):
            # すでにすべて集まっている場合0
            print(0)
            continue

        # BFS開始
        # 状態: state(int)
        # キュー: deque
        # 訪問済み: dictで距離管理 or setで代用しBFSに距離を持たせる

        # 状態の遷移方法
        # 各トレイの「最上部」コップを特定して
        # 移動可能な隣接トレイへ移動する
        # 移動条件:
        # A<->B、B<->Cのみ直接移動可能、A<->Cの移動は禁止

        # 上のコップを特定する方法:
        # 各トレイに属するコップの中で番号最大のコップが上のコップ。

        # さらに移動先トレイのトップコップが移動コップより大きいか、空ならOK

        # まず状態からトレイごとに属するコップを集める
        # そこから最大値で上のコップを決定

        # さらに移動して構造を維持（昇順）（大きいコップの上に小さいは置けない）
        # つまり、移動先トレイのトップコップの番号が移動コップの番号より大きいかどうかを確認

        # == 実装 ==

        # トレイ間の隣接関係（移動可能な方向）
        # A(0)<->B(1), B(1)<->C(2)
        neighbors = {0:[1], 1:[0,2], 2:[1]}

        # BFS初期化
        from collections import deque
        q = deque()
        visited = dict()

        q.append((state, 0))
        visited[state] = 0

        ans = -1

        while q:
            cur, dist = q.popleft()
            if dist > m:
                # m回以内でなければ探索打ち切り
                continue
            if is_goal(cur):
                ans = dist
                break

            # 集合の作成: トレイごとのコップ
            tray_cup_lists = {0:[],1:[],2:[]}
            for i in range(n):
                pos = get_pos(cur, i)
                tray_cup_lists[pos].append(i)  # iは0-basedコップ番号

            # 各トレイの上のコップ（最大番号）を特定
            # 番号が大きいほど上
            upper_cup = dict()
            for t in range(3):
                if tray_cup_lists[t]:
                    upper_cup[t] = max(tray_cup_lists[t])
                else:
                    upper_cup[t] = None  # 空

            # 移動可能なコップ＝それぞれのトレイの上へ行く

            # 上コップを動かしうるトレイから移動する
            for fr in range(3):
                cu = upper_cup[fr]
                if cu is None:
                    continue
                # 移動可能先を探索
                for to in neighbors[fr]:
                    # 移動先の上コップ
                    top_to = upper_cup[to]

                    # 移動するコップ番号は cu (0-based)
                    # トレイ上コップは小さい番号ほど小さいコップ
                    # 規則2により、大きいコップの上に小さいコップを置くのはダメ
                    # つまり移動コップの番号 < トレイtoの上コップ番号 なら不可
                    # (=移動コップより小さいコップを上に置けない)
                    # しかし番号が大きいほど大きいコップと問題文 (
                    # 小さいコップが一番下、一番大きいコップ上)

                    # コップ番号は1-basedで大きいほどサイズが大きいと問題文
                    # クラスター表示は0-basedコップ番号だが大きいほどコップは大きい
                    # なので、
                    # 移動コップ番号 < top_to なら移動可能 （移動コップは小さいコップで上に乗るのはより大きい上コップだから）
                    # → 違う、top_toがNoneなら積める（空）
                    # → ここで一旦昇順重ねを考える

                    # 問題文の昇順の定義: 小さいコップが下、大きいコップが上
                    # 移動先トレイの上部コップ番号が大きい（top_to > cu)なら
                    # 移動コップ(小さい)を上に乗せられない
                    # なので、
                    # 移動コップ (cu) が top_to より大きい → OK
                    # 移動コップが大きい（番号が大きい）=上に置いてもOK
                    # (大は上、so,新たに置くコップ番号 >= top_to)

                    # まとめると、移動先の上コップ番号がNone（空）ならOK
                    # そうでなければ、移動コップ番号 > top_to ならOK

                    if top_to is None or cu > top_to:
                        # 有効な遷移
                        nxt = set_pos(cur, cu, to)

                        if nxt not in visited or visited[nxt] > dist + 1:
                            visited[nxt] = dist +1
                            q.append((nxt, dist+1))

        print(ans)

if __name__ == "__main__":
    main()