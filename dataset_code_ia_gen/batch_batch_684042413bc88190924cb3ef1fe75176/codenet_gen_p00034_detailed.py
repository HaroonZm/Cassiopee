# 鉄道路線すれ違い判定プログラム
# 問題: 複線の路線で両端から速さv1, v2で同時に出発した2列車がどの区間で
#        すれ違うかを求める。駅でのすれ違いは区間番号が小さい方を採用。

def main():
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # 入力の例：
        # 1,1,1,1,1,1,1,1,1,1,40,60
        # 区間長 l1,l2,...l10 と速度 v1,v2 がカンマ区切りで並ぶ

        parts = line.split(',')
        if len(parts) != 12:
            # 12個でないなら無効行としてスキップ
            continue

        # 区間長と速度を整数として取得
        lengths = list(map(int, parts[:10]))  # l1 ~ l10
        v1, v2 = map(int, parts[10:12])       # v1, v2

        # 鉄道路線長さの累積和を求める（駅の距離位置）
        # station_pos[i]は駅iの位置(km)
        # 駅0が左端終端駅、駅10が右端終端駅と仮定
        station_pos = [0]
        for l in lengths:
            station_pos.append(station_pos[-1] + l)
        total_length = station_pos[-1]

        # 両端から出発し、時間tでの各列車の位置は
        # left_train_pos = v1 * t  (km)
        # right_train_pos = total_length - v2 * t (km)

        # すれ違うとは left_train_pos >= right_train_pos の時点で初めてすれ違う

        # すれ違い時間 t_guess は
        #     v1 * t = total_length - v2 * t
        #     t = total_length / (v1 + v2)
        t_cross = total_length / (v1 + v2)

        left_pos = v1 * t_cross
        right_pos = total_length - v2 * t_cross

        # left_pos と right_pos は理論上ほぼ等しい（すれ違い点）

        # この位置がどの区間に入るか判定
        # 区間iは区間番号i=1..10であり、区間iは駅 i-1 と 駅 i の間
        # 駅位置は station_pos[i]

        # 駅上でのすれ違い判定
        # すれ違い位置がぴったり駅の位置なら、区間番号は両側区間の小さい方を使う
        import bisect

        # 1. 駅位置配列 station_pos と一致するか判定
        # left_pos は左からの距離 (km)

        # 駅iの位置と一致したら、すれ違い区間番号はi(小さい方の区間番号)、ただし駅0は範囲外なので注意
        idx = bisect.bisect_left(station_pos, left_pos)

        if idx < len(station_pos) and abs(station_pos[idx] - left_pos) < 1e-10:
            # 駅でのすれ違い
            # 駅idxでのすれ違いなので区間番号は idx または idx-1 の小さい方
            # 駅0は左端終端駅なので区間番号は1となる
            # 駅10は右端終端駅なので区間番号は10となる
            if idx == 0:
                cross_section = 1
            elif idx == len(station_pos) - 1:
                cross_section = 10
            else:
                # 両側の区間は idx (右側区間) と idx (左側区間は idx)
                # 駅iに隣接する区間は i (右側) と i (左側)か見極め
                # 駅iに接する区間は  i (駅i〜駅i+1) と i (駅i-1〜駅i)
                # 区間番号は  idx と idx (同じ数値...)
                # 整理すると、駅iの左側区間はi (駅i-1->駅i), 右側区間はi+1 (駅i->駅i+1)となるため、片側小さい方の番号はi
                # ただし、idxは駅の位置index、駅番号＝idx
                # 区間は駅番号-1→駅番号が区間番号なので駅iと駅i-1間の区間は i 番
                # 駅iの左側区間は i 番
                # 駅iの右側区間は i+1 番（i+1が最大で10）
                # 小さいほうは i (左側区間) となる
                cross_section = idx
        else:
            # 駅上でない場合はすれ違い点の区間を特定
            # left_pos は区間番号 idx と idx+1 の間
            # bisect_right のほうが適切で、left_pos が station_pos[i] より大きい最大の i を探す
            # station_pos は昇順なので
            cross_section = bisect.bisect_right(station_pos, left_pos)
            # bisect_right は区間番号に対応するので、区間番号 = cross_section
            # cross_section は 1〜10 のはず
            # 左端駅は station_pos[0] なので区間番号1が左端区間となる

            # bisect_right は区間番号を表すので区間番号としてそのまま使う

        # 出力
        print(cross_section)

if __name__ == '__main__':
    main()