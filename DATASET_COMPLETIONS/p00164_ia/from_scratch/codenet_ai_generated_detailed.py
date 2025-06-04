# -*- coding: utf-8 -*-

# 初期のこりおはじき数
INITIAL_MARBLES = 32

def simulate_game(a):
    """
    次郎君の数列 a に基づいて、おはじき取りゲームをシミュレートする関数。

    引数:
        a: 次郎君の決めた数列（リスト）

    戻り値:
        各手番後のおはじきの残り数のリスト
    """
    # ゲーム開始時のおはじき数
    marbles = INITIAL_MARBLES
    result = []

    # 次郎君の数列の長さ
    n = len(a)

    # 次郎君の数列にアクセスするためのインデックス
    jiro_idx = 0

    # プレイヤーの交代は、Trueを一郎君（兄）、Falseを次郎君として判別
    # 一郎君の番からスタート
    ichiro_turn = True

    while marbles > 0:
        if ichiro_turn:
            # 一郎君の必勝法：(n-1) % 5 個だけ取る
            take = (marbles - 1) % 5
            if take == 0:
                take = 1  # 余りが0の時は最低1個取ることにする（実際は常に1-4個取る）
        else:
            # 次郎君は数列 a による
            take = a[jiro_idx]
            jiro_idx = (jiro_idx + 1) % n
            # 残り個数以下ならそのまま、以上なら残り全部取る
            if take > marbles:
                take = marbles

        # おはじきを取った後の残数を記録
        marbles -= take
        result.append(marbles)

        # 次のターンは相手の番
        ichiro_turn = not ichiro_turn

    return result


def main():
    import sys

    lines = sys.stdin.read().strip().split('\n')

    # 入力の読み込みと処理
    i = 0
    while True:
        if i >= len(lines):
            break
        n_line = lines[i].strip()
        i += 1
        if n_line == '0':
            break
        n = int(n_line)
        a_line = lines[i].strip()
        i += 1
        a = list(map(int, a_line.split()))
        # シミュレーション
        result = simulate_game(a)
        # 出力
        for r in result:
            print(r)

if __name__ == "__main__":
    main()