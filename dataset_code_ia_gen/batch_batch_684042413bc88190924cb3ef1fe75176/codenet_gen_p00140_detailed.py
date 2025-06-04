# バス路線の経路探索問題を解くプログラム
# 停留所は0〜9までの10箇所。
# 停留所0では折り返し（行きと帰りが逆向き）、停留所5〜9は循環路線になっている。
# 停留所1〜5では2方向バス利用可。より短い経路の方向で移動。
# 同じ停留所を乗車・降車に指定しない。

def solve_bus_routes():
    import sys

    # 0〜9 の停留所について、2方向の路線をモデル化する。
    # 進行方向1(左方向)：0→1→2→3→4→5→6→7→8→9→5（循環）と考える。
    # 実際は0のみ折り返し。5〜9は循環。1〜5はどちら方向にも行ける。
    
    # 左方向の路線（0→1→2→3→4→5→6→7→8→9→5 循環）
    # 0から5までは左方向で進むとする。
    # 右方向の路線は折り返しで、0で折り返すので左方向の逆。つまり 0←1←2←3←4←5 とみなす。
    # 5〜9は循環だから、5→6→7→8→9→5 （循環）

    # 左方向の経路をリストで定義（循環部分は5以降ループ）
    left_route = [0,1,2,3,4,5,6,7,8,9]

    # 右方向の経路は0で折り返すため、0〜5は逆順: 5→4→3→2→1→0
    # 5〜9は循環。この循環を右方向とみる場合は5→9→8→7→6→5となるが問題文で5→6→7→8→9→5が循環なので
    # 右方向で循環は逆回り：5→9→8→7→6→5

    # 左方向と右方向のルート（停留所数は10）
    # 左方向: 0->1->2->3->4->5->6->7->8->9->5...
    # 右方向: 0->1->2->3->4->5->9->8->7->6->5...

    # よって、左方向の一周は 0 1 2 3 4 5 6 7 8 9 循環5以降
    # 右方向の一周は 0 1 2 3 4 5 9 8 7 6 循環5以降で逆向き循環

    # ここで、乗車停留所s,降車停留所tに対し、1~5の停留所であれば短い方の方向で移動。
    # それ以外は方向は固定となる。

    # 停留所0は折返し点なので、
    # 乗車時s=0なら左方向（0→1→2→...）
    # 乖離避けるために、s or tが5~9なら循環ルート上の短いほうの経路を使う。

    # バス路線の特徴から、以下の判断を行い経路を求める。

    def get_left_path(s, t):
        # 左方向（0→1→2→3→4→5→6→7→8→9）での経路を取得
        # 5から先は循環
        path = []
        current = s
        path.append(current)
        while current != t:
            if current < 5:
                current +=1
            else:
                current = current +1 if current < 9 else 5
            path.append(current)
        return path

    def get_right_path(s, t):
        # 右方向（0←1←2←3←4←5 かつ 5→9→8→7→6→5 循環）での経路を取得
        path = []
        current = s
        path.append(current)
        while current != t:
            if current <=5 and current >0:
                # 停留所1～5 は折返しで0に戻る方向
                current -=1
            elif current >=6:
                # 5～9の循環は5→9→8→7→6→5 と逆回り
                if current ==5:
                    current =9
                else:
                    current -=1
            else:
                # current ==0
                current =1  # 右方向の0は普通使わないが安全処理
            path.append(current)
        return path

    def dist_left(s,t):
        # 左方向の距離
        count =0
        current = s
        while current != t:
            if current <5:
                current +=1
            else:
                current = current+1 if current <9 else 5
            count +=1
        return count

    def dist_right(s,t):
        # 右方向の距離
        count =0
        current = s
        while current != t:
            if current <=5 and current >0:
                current -=1
            elif current >=6:
                if current ==5:
                    current =9
                else:
                    current -=1
            else:
                current =1
            count +=1
        return count

    input = sys.stdin.readline
    n = int(input())

    for _ in range(n):
        s_str, t_str = input().split()
        s = int(s_str)
        t = int(t_str)

        # 乗車降車は同じ停留所ではないと仮定
        # 1～5の停留所であれば、左方向・右方向どちらも乗車可能
        # より短い経路の方向で移動

        if s == t:
            # 問題文で乗車・降車は異なるため通常不要
            print(s)
            continue

        # 0は折り返し点なので左方向と右方向の判断は固定的に行う。
        # また、1～5は双方向乗車可。その他は経路固定。

        # 以下の方針で方向決定
        # s,t が共に1~5の範囲なら短い方の経路を選ぶ
        # s or t が0の場合は左方向（0→1→...）に固定
        # s or t が6~9のみの場合は循環路線で最短経路を選ぶ

        # 1～5の区間かどうか確かめる
        def in_1_5(x):
            return 1 <= x <=5

        def in_6_9(x):
            return 6 <= x <=9

        if in_1_5(s) and in_1_5(t):
            # 1～5間なら左か右か短い距離を選択
            d_l = dist_left(s,t)
            d_r = dist_right(s,t)
            if d_l <= d_r:
                path = get_left_path(s,t)
            else:
                path = get_right_path(s,t)
        elif s==0 or t==0:
            # 0は折り返し点で左方向固定
            path = get_left_path(s,t)
        elif in_6_9(s) or in_6_9(t):
            # 循環路線区間なら左・右どちらか短い方を選択
            d_l = dist_left(s,t)
            d_r = dist_right(s,t)
            if d_l <= d_r:
                path = get_left_path(s,t)
            else:
                path = get_right_path(s,t)
        else:
            # その他の場合（例: s,tのいずれかが5）
            # 5は1～5の範囲ではないが1～5と6～9の境界。5は1~5に含めて双方向乗車可扱いも可能。
            # 問題文では1～5は双方向乗車可。5は1～5に含めるのでここの条件はそのものか。
            # よって、このelseは本来ありえないが念のため左方向をとる。
            path = get_left_path(s,t)

        print(' '.join(map(str,path)))

if __name__ == "__main__":
    solve_bus_routes()