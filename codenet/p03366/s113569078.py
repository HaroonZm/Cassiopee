#!/usr/bin/python

import sys,collections,itertools,re,math,fractions,decimal,random,array,bisect,heapq

# decimal.getcontext().prec = 50
# sys.setrecursionlimit(10000)
# MOD = 10**9 + 7

def solve(f):
    n, s = f.read_int_list()
    x = [f.read_int_list() for _ in xrange(n)]

    ans = 0
    side = 0
    l = 0
    r = n-1
    while True:
        if x[l][0] > s:
            return ans + x[r][0] - s
        elif x[r][0] < s:
            return ans + s - x[l][0]
        else:
            if x[l][1] >= x[r][1]:
                x[l][1] += x[r][1]
                if side != 1:
                    ans += x[r][0] - x[l][0]
                side = 1
                r -= 1
            else:
                x[r][1] += x[l][1]
                if side != -1:
                    ans += x[r][0] - x[l][0]
                side = -1
                l += 1

class Reader(object):
    def __init__(self, filename=None):
        self.file = open(filename) if filename is not None else None
        self.case = 1

    def __readline(self):
        return self.file.next().strip() if self.file else raw_input()

    def next_case(self):
        self.file.next()
        self.case += 1

    def read_int(self): return int(self.__readline())
    def read_float(self): return float(self.__readline())
    def read_long(self): return long(self.__readline())
    def read_decimal(self): return decimal.Decimal(self.__readline())
    def read_str(self): return self.__readline()

    def read_int_list(self): return map(int, self.__readline().split())
    def read_float_list(self): return map(float, self.__readline().split())
    def read_long_list(self): return map(long, self.__readline().split())
    def read_decimal_list(self): return map(decimal.Decimal, self.__readline().split())
    def read_str_list(self): return self.__readline().split()

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    f = Reader(filename)
    if f.file:
        while True:
            print "Case #%d\n"%f.case, solve(f)
            try:
                f.next_case()
            except StopIteration:
                break
    else:
        print solve(f)