import sys
from datetime import date

def solve(data):
    y1, m1, d1, y2, m2, d2 = data
    date1 = date(y1, m1, d1)
    date2 = date(y2, m2, d2)
    return (date2 - date1).days

def main(args):
    while True:
        data = [int(x) for x in input().split()]
        try:
            print(solve(data))
        except ValueError:
            break

if __name__ == '__main__':
    main(sys.argv[1:])