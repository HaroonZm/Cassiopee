import sys
from sys import stdin

input = stdin.readline

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        visitors = {
            'under10': 0,
            '10s': 0,
            '20s': 0,
            '30s': 0,
            '40s': 0,
            '50s': 0,
            '60s+': 0
        }
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

def main2(args):
    while True:
        n = int(input())
        if n == 0:
            break
        age = [0] * 13
        for _ in range(n):
            a = int(input())
            age[a // 10] += 1
        print(age[0])
        print(age[1])
        print(age[2])
        print(age[3])
        print(age[4])
        print(age[5])
        print(sum(age[6:]))

if __name__ == '__main__':
    main2(sys.argv[1:])