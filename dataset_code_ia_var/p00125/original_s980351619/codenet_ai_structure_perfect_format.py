import sys
from datetime import date

def solve(data):
    y1, m1, d1, y2, m2, d2 = data
    date1 = date(y1, m1, d1)
    date2 = date(y2, m2, d2)
    delta = date2 - date1
    return delta.days

def main(args):
    while True:
        try:
            data = [int(x) for x in input().split()]
            if not data or len(data) != 6:
                break
            result = solve(data)
            print(result)
        except:
            break

if __name__ == '__main__':
    main(sys.argv[1:])