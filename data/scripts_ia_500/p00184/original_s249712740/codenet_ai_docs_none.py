import sys
from sys import stdin
from collections import defaultdict
input = stdin.readline

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        visitors = defaultdict(int)
        for _ in range(n):
            age = int(input())
            if age < 10:
                visitors['under10'] += 1
            elif age < 20:
                visitors['10s'] += 1
            elif age < 30:
                visitors['20s'] += 1
            elif age < 40:
                visitors['30s'] += 1
            elif age < 50:
                visitors['40s'] += 1
            elif age < 60:
                visitors['50s'] += 1
            else:
                visitors['60s+'] += 1
        print(visitors['under10'])
        print(visitors['10s'])
        print(visitors['20s'])
        print(visitors['30s'])
        print(visitors['40s'])
        print(visitors['50s'])
        print(visitors['60s+'])

if __name__ == '__main__':
    main(sys.argv[1:])