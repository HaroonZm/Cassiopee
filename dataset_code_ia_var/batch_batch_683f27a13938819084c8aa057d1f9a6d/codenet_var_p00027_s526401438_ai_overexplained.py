#!/usr/bin/env python

# インポート(Import)部: 必要な標準ライブラリをプログラムに取り込む
# sysモジュールは標準入力・出力などシステム関連の機能を提供します
import sys

# datetimeモジュールは日付や時間を扱うためのライブラリです
import datetime

# 関数 'get_weekday' の定義
# この関数は月(month)と日(day)の2つの整数型引数を受け取り、その日付の曜日名(英語)を返します
def get_weekday(month, day):
    # タプル 'weekdays' を作成します
    # これは各曜日の英語名が順に格納された「変更不可能な」リストです
    # 曜日の順番はdatetime.date.weekday()の戻り値(0:月曜,1:火曜,...)と一致させています
    weekdays = (
        "Monday",    # 月曜日
        "Tuesday",   # 火曜日
        "Wednesday", # 水曜日
        "Thursday",  # 木曜日
        "Friday",    # 金曜日
        "Saturday",  # 土曜日
        "Sunday"     # 日曜日
    )
    # 年を2004年で固定してdatetime.dateオブジェクトを作成します
    # この年は月日が入力されれば曜日が問題なく判定できるうるう年です
    # datetime.date(year, month, day): 指定した年月日の日付オブジェクトを生成します
    date_obj = datetime.date(2004, month, day)
    # .weekday()メソッドはその日が何曜日かを整数値(0〜6)で返します。0は月曜,6は日曜です
    weekday_index = date_obj.weekday()
    # 上記の整数値でタプル 'weekdays' から対応する曜日の英語名を取得して返します
    result = weekdays[weekday_index]
    return result

# メイン処理を担うmain()関数を定義します
def main():
    # 無限ループを使って入力を繰り返し処理します
    # 'while 1' は'while True'と同じ意味で常に真となります
    while 1:
        # sys.stdin.readline() で1行入力を取得します（改行を含む）
        # 例: "5 3\n"
        s = sys.stdin.readline()
        # 入力された文字列をスペースで分割しリストにします
        # 例: "5 3\n".split(" ") -> ["5", "3\n"]
        splitted = s.split(" ")
        # 各要素をint()で整数型に変換します
        # ["5", "3\n"] -> [5, 3]（intは末尾の改行や空白を自動的に無視します）
        month, day = [int(x) for x in splitted]
        # 月が0の場合、これは入力の終了を示します
        # このときは何も出力せず、return文でmain()を終了します
        if month == 0:
            return
        # get_weekday関数で曜日名を取得し出力します
        # print文(このコードはPython2用でカッコを使っていません)
        print get_weekday(month, day)

# このif文はPythonプログラムが直接実行されたときのみmain()を呼び出します
# 'import'された場合はmain()を実行しません
if __name__ == '__main__':
    main()