# 踏み台昇降問題の解法
# ここでは、足の動きを時系列で追いながら、状態遷移を管理して正しい昇降回数をカウントする。
# 状態は「両足床状態(both_on_floor)」か「両足踏み台状態(both_on_step)」のいずれか。
# 昇降1回は下記2種のいずれかでカウントされる：
# 1. 両足床→両足踏み台への移行（左足と右足のどちらかを先に上げて、片方を上げた状態を経て両方踏み台へ）
# 2. 両足踏み台→両足床への移行（左足と右足のどちらかを先に下げて、片方を下げた状態を経て両方床へ）
# 片足ずつの単独昇降のみはカウントしない。

import sys

def main():
    for line in sys.stdin:
        n_line = line.strip()
        if not n_line:
            continue
        n = int(n_line)
        if n == 0:
            # 入力の終わり
            break
        movements_line = sys.stdin.readline().strip()
        movements = movements_line.split()

        # 初期状態：両足とも床にある
        # 足の状態を管理：
        # 0：床、1：踏み台
        left = 0
        right = 0

        # 昇降の1回は、両足が床or踏み台の状態から、両足とも逆の状態になる時点でカウント
        count = 0

        # 状態遷移は下記を考慮
        # 片足ずつ上下していき、片方だけが動いた中間状態は昇降完了とはみなさない
        # 両足の状態が同じ→片足だけ動く→両足の状態が逆に揃う→1回カウント

        # 状態の遷移に注目：前回両足が同じ高さだった状態(left == right)
        # 今回の動きで片足だけ変わる中間状態
        # 次の動きで両足とも逆の高さになる状態に遷移したらカウント

        # つまり、両足が同じ床か踏み台かの状態からスタートし、
        # 左または右片方づつ動かしていき、両足が一緒の状態（床か踏み台）に戻ったとき、
        # それが前の状態と逆ならカウントアップ

        prev_both_same = (left == right)  # 初期状態ではTrue（共に床=0）
        prev_same_state = left  # どちらかの状態で良い。0なら床状態、1なら踏み台状態

        for move in movements:
            foot = move[0]  # l or r
            action = move[1]  # u or d

            # 足の位置を更新
            if foot == 'l':
                # 左足の上下を更新
                if action == 'u':
                    left = 1
                else:
                    left = 0
            else: # foot == 'r'
                if action == 'u':
                    right = 1
                else:
                    right = 0

            # 両足が同じ高さか判定
            both_same = (left == right)

            if both_same:
                # 両足とも同じ（床 or 踏み台）
                # かつ、前の両足同じ状態と違う状態なら昇降1回とみなす
                if prev_both_same and prev_same_state != left:
                    count += 1
                # 状態更新
                prev_same_state = left
                prev_both_same = True
            else:
                # 両足が異なる中間状態
                prev_both_same = False

        print(count)

if __name__ == "__main__":
    main()