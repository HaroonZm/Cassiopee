N = int(input())
table = [input() for _ in range(N)]

# 対応関係をまとめる
# win_map[i] = [j for j in range(N) if iがjに勝つ]
win_map = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if table[i][j] == 'o':
            win_map[i].append(j)

# ここでは単純に、相手の手がわからないので、
# 前回の相手の手に勝てる手を出す簡易戦略を使用する。
# 1回目はランダムに1を出し、2回目以降は相手の直前の手に勝つ手を出す。

import sys

prev_judge_hand = None

for turn in range(1000):
    if turn == 0:
        candidate = 0  # 1手目はとりあえず手1（0-indexで0）
    else:
        # 相手の前の手に勝てる手があればランダムに選ぶ（ここは単純に最初の1つを選択）
        winning_hands = win_map[prev_judge_hand]
        if winning_hands:
            candidate = winning_hands[0]
        else:
            candidate = 0  # もし勝てる手がなければ手1

    print(candidate + 1)
    sys.stdout.flush()

    prev_judge_hand = int(input()) - 1  # 1-indexedなので0-indexに変換