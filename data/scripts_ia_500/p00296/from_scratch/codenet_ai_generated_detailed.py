import sys
sys.setrecursionlimit(10**7)

# この問題は円形に並んだ生徒たちから、指定された方向に指定された回数だけバトンを渡して、
# バトンを受け取った生徒を脱落させ、その後バトンは脱落した生徒の時計回り隣に渡す操作を繰り返すというもの。
# 脱落した生徒は円から抜けるため、生徒の数は少しずつ減るが、残っている生徒の順番は円形に繋がっているまま。

# これを効率良くシミュレーションするには、単純なリストからの削除や回転は遅い為、
# 循環双方向連結リスト（double linked list）を用いることが適切。
# 各生徒の前後の生徒を管理し、脱落で削除し、次のバトン保持者を決める操作を高速化する。

# N: 生徒数
# M: 脱落させる回数
# Q: 質問数

N, M, Q = map(int, input().split())
a_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

# 循環双方向連結リストの前後の要素を表す配列
prev = [0]*N
next = [0]*N

# 初期化：0からN-1までの生徒が円形に並ぶ
for i in range(N):
    prev[i] = (i-1) % N
    next[i] = (i+1) % N

# alive配列で生存状態を管理。True: 生存, False: 脱落
alive = [True]*N

# 最初は生徒0がバトンを持つ
current_holder = 0

for a in a_list:
    # バトンを持つ生徒がaを宣言
    # aが偶数なら時計回り（next方向）、奇数なら反時計回り（prev方向）にa回分バトンを渡す
    # つまりa回移動して到達した生徒が脱落する

    if a % 2 == 0:
        # 偶数 - 時計回り移動
        for _ in range(a):
            current_holder = next[current_holder]
    else:
        # 奇数 - 反時計回り移動
        for _ in range(a):
            current_holder = prev[current_holder]

    # current_holderが脱落する生徒
    eliminated = current_holder
    alive[eliminated] = False

    # 脱落した生徒の前後をつなぎ直す
    # prev[eliminated] と next[eliminated] を繋げて、eliminatedをリストから除去
    prev_of_elim = prev[eliminated]
    next_of_elim = next[eliminated]

    next[prev_of_elim] = next_of_elim
    prev[next_of_elim] = prev_of_elim

    # 脱落した生徒の時計回り隣の生徒にバトンを渡す（次のバトン保持者）
    current_holder = next_of_elim

# 最後に残った生徒は掃除免除
# aliveがTrueである生徒たち

# 質問 q_listに対して、その生徒が免除されるかどうかを1 or 0で出力
for q in q_list:
    print(1 if alive[q] else 0)