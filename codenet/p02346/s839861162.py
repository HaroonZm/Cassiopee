#!/usr/bin/env python

"""
input:
3 5
0 1 1
0 2 2
0 3 3
1 1 2
1 2 2

output:
3
2
"""

import sys

class BinaryIndexedTree(object):
    __slots__ = ('length', 'dat')

    def __init__(self, n):
        """
        Init a BIT with update and find for range sum queries.
        """
        self.length = int(n)
        self.dat = [0] * (self.length + 1)

    # sum(A[1] ... A[i])
    def __init_sum(self, i):
        _sum = 0
        while i > 0:
            _sum += self.dat[i]
            i -= i & (-i)
        return _sum

    def get_sum(self, s, t):
        return self.__init_sum(t) - self.__init_sum(s - 1)

    # A[i] += x
    def get_add(self, i, x):
        while i <= self.length:
            self.dat[i] += x
            i += i & (-i)
        return None

def action(cmd_list):
    case = BinaryIndexedTree(n_num)
    
    for query in cmd_list:
        cmd, ele_1, ele_2 = map(int, query)
        if cmd == 0:
            case.get_add(ele_1, ele_2)
        elif cmd == 1:
            res = case.get_sum(ele_1, ele_2)
            print(res)

    return case

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    n_num, q_num = map(int, _input[0].split())
    q_list = map(lambda x: x.split(), _input[1:])

    ans = action(q_list)