"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0125
"""
import sys
from datetime import timedelta, date

def solve(data):
    y1, m1, d1, y2, m2, d2 = data
    date1 = date(y1, m1, d1)
    date2 = date(y2, m2, d2)
    delta = date2 - date1
    return delta.days

def main(args):
    while True:
        data = [int(x) for x in input().split()]
        try:
            result = solve(data)
            print(result)
        except ValueError:
            break

if __name__ == '__main__':
    main(sys.argv[1:])