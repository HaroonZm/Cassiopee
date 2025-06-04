n = int(input())
for _ in range(n):
    start, end = map(int, input().split())

    if start == end:
        continue  # 問題文より同じ停留所は指定されないが念のため

    # 乗車停留所と降車停留所が共に1～5の範囲内か判定
    can_choose_direction = (1 <= start <= 5) and (1 <= end <= 5)

    if can_choose_direction:
        # 左方向（降車停留所が停留所0向けの順路）
        # 左方向はここでは start -> start-1 -> ... -> end の順 (ただし0未満は通らない)
        if start > end:
            left_path = list(range(start, end - 1, -1))
        else:
            # start <= end の場合、左方向の意味はstartから0経由でendに行くことだが
            # 0は終点なので0以下で止まる。なので実質右回りとして考える。
            left_path = None

        # 右方向（循環路線側へ向かう経路）
        # 右方向はstart -> start+1 ... -> 5 -> 6 -> 7 -> 8 -> 9 -> 5 -> ... と循環
        # 5～9は循環路線。1～5は1→2→3→4→5と進むと考える。
        # ここでは1～5の範囲で右方向へ行く場合start < endの場合は素直に増加で進む
        # 端の5から6に向かうと循環開始
        def right_route(s, e):
            path = [s]
            current = s
            while current != e:
                if current == 0:
                    # 0では折り返しなので0から右に行くのはなし（問題設定上0は通行不可右回り）
                    break
                if 1 <= current < 5:
                    current += 1
                elif current == 5:
                    current = 6
                elif 6 <= current < 9:
                    current += 1
                elif current == 9:
                    current = 5
                else:
                    break
                path.append(current)
            return path

        right_path = right_route(start, end)

        # 左パスは存在しなければ無視
        if left_path is None:
            chosen_path = right_path
        else:
            # パスの長さを比較、短い方を選ぶ
            if len(left_path) <= len(right_path):
                chosen_path = left_path
            else:
                chosen_path = right_path
    else:
        # 乗車または降車が1～5の範囲外(0や6~9)
        # 経路は一方向のみ（右回り循環か0折り返し）
        # 0では折り返すため0には直接循環路線側の進行はないため
        # start < end なら普通に増加で進む、それ以外は左方向で減少する
        # ただし6～9は循環路線 → 循環路線内でのループをする
        def path_normal(s, e):
            path = [s]
            current = s
            if s == 0:
                # 0で降車停留所へは逆方向しかない（左方向）
                if e < s:
                    # 左方向は単純な減少
                    for i in range(s - 1, e - 1, -1):
                        path.append(i)
                else:
                    # 出発が0で降車が5～9は右回り経路（循環）になるが0では折り返しのため
                    # 0から直接6に行けないため、反対側循環経路からのアプローチと同じにする
                    # 0発の右回りは無いので左方向のみ利用
                    for i in range(s - 1, e - 1, -1):
                        if i < 0: break
                        path.append(i)
            elif 1 <= s <= 5:
                # 1~5までなら普通に増減比較
                if s <= e:
                    for i in range(s + 1, e + 1):
                        path.append(i)
                else:
                    for i in range(s - 1, e - 1, -1):
                        path.append(i)
            else:
                # 循環路線6～9
                current = s
                while current != e:
                    if current == 9:
                        current = 5
                    else:
                        current += 1
                    path.append(current)
            return path

        chosen_path = path_normal(start, end)

    print(*chosen_path)