"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0565

"""
import sys
from sys import stdin
input = stdin.readline

def main(args):
    pastas = [int(input()) for _ in range(3)]
    drinks = [int(input()) for _ in range(2)]
    total = min(pastas) + min(drinks) - 50
    print(total)

if __name__ == '__main__':
    main(sys.argv[1:])