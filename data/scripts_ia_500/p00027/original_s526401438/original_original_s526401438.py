#!/usr/bin/env python

import sys
import datetime

"""
Input
    複数のデータセットを処理しなければなりません。
    １つのデータセットに月と日が１つのスペース区切られて１行に与えられます。
    月が 0 となったとき入力の最後とします
    （この場合は処理をしないでプログラムを終了させる）。

Output
    各データセットごとに曜日を英語で１行に出力して下さい。
    以下の訳を参考にして出力して下さい。

    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
"""

def get_weekday(month, day):
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    return weekdays[datetime.date(2004, month, day).weekday()]

def main():
    while 1:
        s = sys.stdin.readline()
        month, day = [int(x) for x in s.split(" ")]
        if month == 0:
            return
        print get_weekday(month, day)

if __name__ == '__main__':
    main()