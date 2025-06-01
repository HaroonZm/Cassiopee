"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0164

"""
import sys
from sys import stdin
from itertools import cycle
input = stdin.readline

def taro(n):
    return (n - 1) % 5

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break

        jiro = cycle([int(x) for x in input().split(' ')])

        ohajiki = 32
        while ohajiki > 0:
            ohajiki -= taro(ohajiki)
            print(ohajiki)
            ohajiki -= jiro.__next__()
            print(max(0, ohajiki))

if __name__ == '__main__':
    main(sys.argv[1:])