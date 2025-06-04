import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    # 各電球の点灯可能範囲は [A_i, B_i]
    # 全ての電球の電圧は同じでなければならない
    # 1つの電圧を選んだ時、それを満たす範囲に含まれる電球が点灯可能
    # 最大で何個の電球を同時に光らせられるかを求める問題

    # アプローチ：
    # 電球の点灯範囲の始点と終点を分けて、ラインスイープ法で重複している区間数の最大値を求める
    # 各区間の開始点で +1、終了点の次の位置で -1 としてイベント処理し最大累積値を計算する
    
    events = []
    for A, B in intervals:
        # +1 イベントは区間開始
        events.append((A, 1))
        # -1 イベントは区間終了の次の点で加えることで閉区間を表現 (Bの次の位置)
        events.append((B + 1, -1))

    # イベントを座標で昇順、同じ座標なら +1 イベントを先に処理するためにソート
    events.sort()

    # ラインスイープ実施
    current = 0
    max_on = 0
    for _, delta in events:
        current += delta
        if current > max_on:
            max_on = current

    print(max_on)

if __name__ == "__main__":
    main()