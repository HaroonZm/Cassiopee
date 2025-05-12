"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0158

"""
import sys
from sys import stdin
input = stdin.readline

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break

        count = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n *= 3
                n += 1
            count += 1
        print(count)

if __name__ == '__main__':
    main(sys.argv[1:])