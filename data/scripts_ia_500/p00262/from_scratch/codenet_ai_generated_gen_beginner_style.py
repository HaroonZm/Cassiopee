def is_triangular(num):
    i = 1
    while i * (i + 1) // 2 < num:
        i += 1
    return i if i * (i + 1) // 2 == num else 0

def make_triangle(b):
    total = sum(b)
    k = is_triangular(total)
    if k == 0:
        return -1
    # 目標の形は高さが1からkまで順に増えるリスト
    target = list(range(1, k + 1))
    current = b[:]
    count = 0
    while count <= 10000:
        if current == target:
            return count
        # 一番下の段を全部右端に積み上げる
        bottom_blocks = current[:]
        current = current[len(bottom_blocks):] if len(bottom_blocks) < len(current) else []
        # 実際はlen(bottom_blocks) == len(current)だからcurrentは空になる
        # 問題文の説明だと一番下の段は白いブロックで全部取るのでここはcurrent=空で良い
        current = current[len(bottom_blocks):] if len(bottom_blocks) < len(current) else []
        current = []
        # ずらしたときは一番下の段全てが右端に積まれるので
        # 今回は一番下の段はcurrentのすべてなので、一旦空にしてbottom_blocksを右に積む
        
        # 左に詰める処理としたいが本来は底の段のみを右端に積み上げる処理 必要
        # 理解を単純にするため毎回全部を右端に積みなおす？
        # 正しくは操作の説明通りにする
        # 1. いちばん下のブロックすべて(白いブロック)を取り除き右の端に新しく積み上げる
        # 2. 左に詰める処理をする
        # 実装簡単のため次でやる

        # まず、一番下の段のブロック数は len(current) ではない、 current の中の各要素が段の高さなので、
        # 一番下の段は高さ=1のブロック
        # よって、各位置から高さ1を引く（もしくは1を引けない位置は0にする）これが一番下の段を取り除くこと
        bottom = []
        for x in current:
            if x > 0:
                bottom.append(1)
            else:
                bottom.append(0)
        # bottomを右端に積み上げる
        # currentから一番下の段を取る
        new_current = []
        bottom_sum = 0
        for x in current:
            new_current.append(x - 1 if x > 0 else 0)
        # 左に詰めるため底が0の位置はどうするか
        # 左に寄せると0の区間をなくす
        new_current = [x for x in new_current if x > 0]
        new_current += [0] * (len(current) - len(new_current))
        # bottomは全て1の値をもつ配列なので合計は底の段のブロック数
        bottom_sum = sum(bottom)
        # 右端に積み上げる bottom_sum 個の高さ1ブロックを追加
        new_current += [1] * bottom_sum
        # 0を左に詰めるので右の1段目は続いているので2段目は別列なので今のまま維持
        # 再度高さを左に詰める処理をする
        new_current = [x for x in new_current if x > 0]
        current = new_current
        count += 1
    return -1

while True:
    N = int(input())
    if N == 0:
        break
    b = list(map(int, input().split()))
    total = sum(b)
    k = is_triangular(total)
    if k == 0:
        print(-1)
        continue
    # 目標の形
    target = list(range(1, k+1))
    current = b[:]
    # シンプルに一番下の段を取り除き右に積む
    # 左に詰めるを繰り返すだけの方法を実装
    count = 0
    while count <= 10000:
        if current == target:
            print(count)
            break
        # 一番下の段を取り除き右端に積む
        bottom_count = sum(1 for x in current if x > 0)  # 底の段は高さ1のブロック数
        # 底の段を引く
        current = [x-1 if x > 0 else 0 for x in current]
        # 左に詰める(0を詰める)
        current = [x for x in current if x > 0]
        # 右端に底の段を積む（高さ1のブロックをbottom_count個追加）
        current += [1]*bottom_count
        count += 1
    else:
        print(-1)