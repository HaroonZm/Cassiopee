#!/usr/bin/python

import os
import sys
import math

def solve(f):
    n = f.read_int()
    if n == 0: raise StopIteration
    ary = [f.read_float_list() for _ in xrange(n)]

    x_min = -100.0
    x_max = 100.0

    for _ in xrange(60):
        c1 = (x_min*2 + x_max) / 3
        c2 = (x_min + x_max*2) / 3
        if search_y(ary, c1) > search_y(ary, c2):
            x_max = c2
        else:
            x_min = c1

    return math.sqrt(search_y(ary, x_max))

def search_y(ary, x):
    y_min = -100.0
    y_max = 100.0

    for _ in xrange(60):
        c1 = (y_min*2 + y_max) / 3
        c2 = (y_min + y_max*2) / 3
        if calc(ary, x, c1) > calc(ary, x, c2):
            y_max = c2
        else:
            y_min = c1

    return calc(ary, x, y_max)

def calc(ary, x, y):
    return min([item[2]**2 - (item[0]-x)**2 - (item[1]-y)**2 for item in ary])

class Reader(object):
    def __init__(self, filename=None):
        self.test_mode = filename is not None
        self.cases = 1
        self.buffer = []
        if self.test_mode:
            with open(filename) as f:
                blank_flg = False
                for line in f:
                    line = line.strip()
                    if line:
                        self.buffer.append(line)
                        blank_flg = False
                    else:
                        if not blank_flg: self.cases += 1
                        blank_flg = True

    def __readline(self):
        return self.buffer.pop(0) if self.test_mode else raw_input()

    def read_int(self):
        return int(self.__readline())
    def read_float(self):
        return float(self.__readline())
    def read_long(self):
        return long(self.__readline())
    def read_str(self):
        return self.__readline()

    def read_int_list(self):
        return [int(item) for item in self.__readline().split()]
    def read_float_list(self):
        return [float(item) for item in self.__readline().split()]
    def read_long_list(self):
        return [long(item) for item in self.__readline().split()]
    def read_str_list(self):
        return self.__readline().split()

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv)>1 else None
    f = Reader(filename)
    while True:
        try:
            print solve(f)
        except StopIteration:
            break