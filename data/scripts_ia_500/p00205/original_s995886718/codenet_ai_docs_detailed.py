# グー:1,チョキ:2,パー:3
# 勝ち:1,負け:2,あいこ:3

def determine_rps_outcome(moves):
    """
    5人分のジャンケンの手を受け取り、それぞれの結果を判定する関数。

    引数:
        moves (list of int): 5人それぞれの手を表す整数リスト。1:グー, 2:チョキ, 3:パー

    戻り値:
        list of int: 各人の結果を表すリスト。1:勝ち, 2:負け, 3:あいこ
    """
    # 手ごとの出現数をカウントするリスト。index 0 → グー(1)、1 → チョキ(2)、2 → パー(3)
    lens = [0] * 3
    for move in moves:
        lens[move - 1] += 1

    # あいこの条件チェック
    # グー、チョキ、パーがすべて存在する場合、または同じ手のみで全員が出した場合
    if (lens[0] > 0 and lens[1] > 0 and lens[2] > 0) or (lens[0] == 5 or lens[1] == 5 or lens[2] == 5):
        # 全員あいこ(3)を返す
        return [3] * 5
    else:
        # 結果判定用リスト。indexは手の種類に対応し、値はその手の立場を示す。
        # 1:勝ち, 2:負け, 0:まだ判定されていない
        status = [0] * 3

        # グーが存在する場合
        if lens[0] > 0:
            status[1] = 2  # チョキはグーに負けるので負け(2)
            status[2] = 1  # パーはグーに勝つので勝ち(1)

        # チョキが存在する場合
        if lens[1] > 0:
            status[0] = 1  # グーはチョキに勝つので勝ち(1)
            status[2] = 2  # パーはチョキに負けるので負け(2)

        # パーが存在する場合
        if lens[2] > 0:
            status[0] = 2  # グーはパーに負けるので負け(2)
            status[1] = 1  # チョキはパーに勝つので勝ち(1)

        # 各人の手の結果を返す
        return [status[move - 1] for move in moves]


def main():
    """
    無限ループで標準入力から5つのジャンケンの手を読み込み、
    結果を出力し続ける。

    入力が終了または例外が発生した場合、ループを終了する。
    """
    datas = [0] * 5  # 5人の手を格納するリスト
    while True:
        try:
            # 5人分の手を入力
            for i in range(5):
                datas[i] = int(input())
            # 結果を判定
            results = determine_rps_outcome(datas)
            # 判定結果を出力
            for res in results:
                print(res)
        except:
            # 入力が終了したらループを抜ける
            break


if __name__ == "__main__":
    main()