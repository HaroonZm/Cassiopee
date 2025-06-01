import sys
from sys import stdin
input = stdin.readline

def main(args):
    while True:
        am, pm = map(int, input().split())
        if am == 0 and pm == 0:
            break
        totals = [0] * 5
        totals[0] = am + pm
        for i in range(1, 5):
            am, pm = map(int, input().split())
            totals[i] = am + pm
        top = max(totals)
        shop = totals.index(top)
        print('{} {}'.format(chr(ord('A')+shop), top))

if __name__ == '__main__':
    main(sys.argv[1:])