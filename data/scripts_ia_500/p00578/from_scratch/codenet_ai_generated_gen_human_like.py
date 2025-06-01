n = int(input())
a = list(map(int, input().split()))

# イベントとして、各高さを海面としたときにその区画が沈む（陸地でなくなる）時刻を扱う
# 海面が高さhを超えた時、区画iは沈む（陸地でなくなる）
# 0 <= A[i] <= 10^9 より、海面は0から最大A[i]まで上昇する

# 初期状態（海面0）での島の数を計算する
is_land = [ai > 0 for ai in a]

def count_islands(land):
    count = 0
    prev = False
    for val in land:
        if val and not prev:
            count += 1
        prev = val
    return count

current_islands = count_islands(is_land)
max_islands = current_islands

# 陸地が沈むイベントを海面の高さ昇順に処理する

# 高さとその区画のリストを作成
events = []
for i, height in enumerate(a):
    if height > 0:
        events.append((height, i))

events.sort()

# 海面が上昇していくごとに、区画が沈み、島の数がどう変わるかを更新
for h, i in events:
    if not is_land[i]:
        continue  # すでに沈んでいる場合はスキップ
    # iの区画が沈む
    is_land[i] = False

    left = is_land[i - 1] if i - 1 >= 0 else False
    right = is_land[i + 1] if i + 1 < n else False

    # 島の変化を計算
    # 1. 元はiが陸地だから数には影響している
    # 2. 陸地iが沈むことで島の数はどう変わるか？
    # 条件
    #   連結していた両隣も陸地なら島数は +1 (= 1島が2島に分裂) -> 島数+1
    #   どちらか片方のみ陸地なら島数は変化なし (島が単に短くなる) -> 島数+0
    #   両隣が陸地でなければ島数は-1 (島が消える) -> 島数-1
    if left and right:
        current_islands += 1
    elif not left and not right:
        current_islands -= 1
    # else 現状維持

    if current_islands > max_islands:
        max_islands = current_islands

print(max_islands)