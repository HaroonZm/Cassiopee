# 問題の概要：
# ビデオテープは合計120分（7200秒）です。
# 録画モードは標準（1倍）と3倍録画の2種類あります。
# 入力は現在のカウンタ値（時、分、秒）で与えられ、
# テープを完全に巻き戻し録画開始時は00:00:00です。
# このカウンタ値は標準録画モードでの経過時間を表す。
# テープの残り時間を標準録画モードと3倍録画モードの2つで計算して出力する。

def format_time(total_seconds):
    # 秒を時、分、秒に変換し、2桁表示を保証して文字列化
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def main():
    MAX_STANDARD_SECONDS = 120 * 60  # 7200秒（120分）

    while True:
        # 入力を空白区切りで受け取る（時、分、秒）
        line = input().strip()
        if not line:
            continue  # 空行は読み飛ばす
        H, M, S = map(int, line.split())
        if H == -1 and M == -1 and S == -1:
            break

        # 現在のカウンタ値を秒に変換（標準録画での経過時間）
        elapsed_seconds = H * 3600 + M * 60 + S

        # 残り時間（標準録画モード）
        remain_standard = MAX_STANDARD_SECONDS - elapsed_seconds

        # 残り時間（3倍録画モード）
        # 3倍録画は同じテープ長で3倍録画出来る＝標準録画の1/3の速度でカウントされる。
        # カウンタ値は標準録画モードの経過時間なので、
        # テープ全体の長さは120分×60秒＝7200秒（標準録画時間）
        # 3倍録画では実際に経過したテープ長はelapsed_seconds / 3
        # よってテープの長さ（7200秒）からすでに使ったテープの長さを引くと
        # 残りテープ長は 7200 - elapsed_seconds/3 秒となり、
        # 3倍録画モードの残り録画可能時間はそれの3倍（速度調整）となる。

        # 以下の計算は問題文の出力例から標準録画時間でカウンタが出ているので、
        # 3倍録画モードの残り時間は「テープの総長（7200秒）- elapsed_seconds」×3 とすればOK。
        remain_triple = (MAX_STANDARD_SECONDS - elapsed_seconds) * 3

        # 出力
        print(format_time(remain_standard))
        print(format_time(remain_triple))

if __name__ == "__main__":
    main()