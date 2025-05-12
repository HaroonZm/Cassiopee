"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0220

"""
import sys
from sys import stdin
input = stdin.readline

def solve(f):
    if f >= 256.0:
        return 'NA'
    f *= 16
    int_f = int(f)
    if f != int_f:
        return 'NA'
    bin_f = bin(int_f)[2:]
    fraction_p = bin_f[-4:]
    integer_p = bin_f[:-4]
    return integer_p.zfill(8) + '.' + fraction_p.zfill(4)

def main(args):
    while True:
        f = float(input())
        if f < 0.0:
            break
        result = solve(f)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])