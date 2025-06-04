# 品質検査問題の解法
# 部品は3種類（電源、モーター、ケーブル）に分かれ番号が振られている
# 合格検査の場合、その3部品はすべて正常
# 不合格検査の場合、3部品のうち少なくとも1つは故障
# この条件を満たす正常/故障/不明の分類を行う

def main():
    import sys
    sys.setrecursionlimit(10**7)

    while True:
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0 and c == 0:
            break
        N = int(sys.stdin.readline())
        tests = []
        # 番号範囲
        # 電源: 1 ~ a
        # モーター: a+1 ~ a+b
        # ケーブル: a+b+1 ~ a+b+c
        total_parts = a + b + c

        # 入力を読み込む
        for _ in range(N):
            i, j, k, r = map(int, sys.stdin.readline().split())
            tests.append((i, j, k, r))

        # 部品の状態推定に使う集合
        # normal_candidates: 正常である可能性のある部品集合（間接的な制約用）
        # broken_candidates: 故障である可能性のある部品集合
        # 今回の問題のポイントは矛盾が無ければ、検査結果から確実に故障or正常かを推論すること

        # まず、「合格」検査から各部品は正常である可能性が確実にある（つまり正常ならば矛盾しない）
        # 「不合格」検査は、3つのうち1つ以上が故障。つまりその部品全てが正常なら矛盾。

        # ここで、以下の2フェーズの演繹を行う。

        # 1段階目：合格検査に登場した部品はすべて正常である可能性がある＝正常候補である
        # 2段階目：不合格検査に対して、もしその検査の3部品のうち1つも故障確定でない場合、
        #           1つは故障でなければならないので、少なくとも1つは故障を含む。しかし確定はできないので保留。
        #           逆に不合格検査の部品のうち1つでも正常確定の場合、この分岐を使って故障の可能性を絞りこめる。

        # 実際は確実判定には以下の方法を使う。
        # 状態は3種類で初期は全て不明(2)
        UNKNOWN = 2
        NORMAL = 1
        BROKEN = 0

        state = [UNKNOWN]*(total_parts+1)  # 部品番号1からスタート、state[0]は未使用

        # 合格検査に登場した部品は正常でなければならない => 正常判定
        for i,j,k,r in tests:
            if r == 1:
                # すべて正常
                # 既に故障判定と矛盾すれば矛盾した問題だが問題文ではないとする
                for p in (i,j,k):
                    # 故障判定されていたら矛盾なので注意、ここは問題文前提で発生しないので安心して上書き
                    state[p] = NORMAL

        # 状態を推論するために何度も繰り返し更新
        # 不合格検査では3つのうち1つ以上故障かつ3つすべて正常はだめ
        # つまり不合格検査の3部品のうち全て正常だと矛盾
        # もし不合格検査の3部品のうち2つが正常確定で1つ不明ならその不明は故障確定になる
        # これを繰り返すことで故障・正常判定が増えていく

        updated = True
        while updated:
            updated = False

            for i,j,k,r in tests:
                if r == 0:
                    # 不合格検査
                    s = [state[i], state[j], state[k]]
                    # 3つの状態のうち正常(NORMAL)の数
                    normal_cnt = sum(1 for x in s if x == NORMAL)
                    # 故障(BROKEN)の数
                    broken_cnt = sum(1 for x in s if x == BROKEN)
                    # 不明(UNKNOWN)の数
                    unknown_cnt = sum(1 for x in s if x == UNKNOWN)

                    # 全て正常は矛盾なのでありえない
                    if normal_cnt == 3:
                        # 矛盾があるが問題文前提でないので無処理
                        pass

                    # 故障が判明しているものが1つ以上あればOK → 特に状態更新なし
                    if broken_cnt >= 1:
                        continue

                    # ここから確実に1つは故障が必要だが今はなしなら
                    # 1つのみ不明, 2つ正常なら不明は故障確定
                    if normal_cnt == 2 and unknown_cnt == 1:
                        # 不明の部分を故障に決定
                        for idx, p in enumerate((i,j,k)):
                            if state[p] == UNKNOWN:
                                state[p] = BROKEN
                                updated = True
                                break

                    # 2つ以上不明なら判定できない、スキップ
                    # 1つも正常でないなら、正常が0の可能性もあるが判定不可

        # さらに推論してみる
        # 合格検査の部品は正常確定で、それと触れ合った不合格検査で
        # その不合格検査の他の部品が不明なら故障を確定できる場合がある
        # 上のループだけだと補えない場合もあるため繰り返しで完全に収束させる

        # 二重ループで何度も推論続行
        for _ in range(1000):
            changed = False

            for i,j,k,r in tests:
                if r == 1:
                    # 合格検査なら3つ全部正常
                    for p in (i,j,k):
                        if state[p] == UNKNOWN:
                            state[p] = NORMAL
                            changed = True

                elif r == 0:
                    s = [state[i], state[j], state[k]]
                    normal_cnt = sum(1 for x in s if x == NORMAL)
                    broken_cnt = sum(1 for x in s if x == BROKEN)
                    unknown_cnt = sum(1 for x in s if x == UNKNOWN)

                    # 故障一つ以上必須
                    if broken_cnt == 0:
                        # 故障確定がないなら判定できる限界で推理

                        # 例えば正常2、不明1なら不明が故障確定
                        if normal_cnt == 2 and unknown_cnt == 1:
                            for idx,p in enumerate((i,j,k)):
                                if state[p] == UNKNOWN:
                                    state[p] = BROKEN
                                    changed = True
                                    break

            if not changed:
                break

        # 出力
        # 部品1からtotal_partsまで
        for i in range(1, total_parts+1):
            print(state[i])

if __name__ == "__main__":
    main()