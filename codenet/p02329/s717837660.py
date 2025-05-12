"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_4_A
TLE
"""
import sys
from sys import stdin
from bisect import bisect_right, bisect_left
input = stdin.readline
 
 
def main(args):
    N, V = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    D = [int(x) for x in input().split()]
 
    AB = []
    for i in A:
        for j in B:
           AB.append(i+j)
    AB.sort()
 
    CD = [float('-inf'), float('inf')]
    for i in C:
        for j in D:
           CD.append(i+j)
    CD.sort()
 
    count = 0
    for ab in AB:
        i = bisect_left(CD, V - ab)
        j = bisect_right(CD, V - ab)
        count += max((j-i), 0)
 
    print(count)
 
 
if __name__ == '__main__':
    main(sys.argv[1:])