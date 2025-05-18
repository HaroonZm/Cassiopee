#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

def check(c):
    return (ord(c) >= ord('0') and ord(c) <= ord('9'))

def check2(c):
    return (ord(c) >= ord('A') and ord(c) <= ord('Z'))

while True:
    S1, S2 = raw_input().split()
    if S1 == '0':
        break
    N = int(S2)
    SS = ''
    flag = False
    for i in range(len(S1) - 1):
        SS += S1[i]
        if check(S1[i]) and not check(S1[i + 1]) and S1[i + 1] != '(':
            SS += '('
            flag = True
        elif flag:
            SS += ')'
            flag = False
    SS += S1[len(S1) - 1]
    if flag:
        SS += ')'
    S1 = '(' + SS + ')'
    for i in range(26):
        c = chr(ord('A') + i)
        S1 = S1.replace('(' + c, '("' + c)
        S1 = S1.replace(c + ')', c + '")')
        S1 = S1.replace(')' + c, ')"' + c)
        S1 = S1.replace(c + '(', c + '"(')
        for j in range(10):
            c2 = str(j)
            S1 = S1.replace(c + c2, c + '"' + c2)
    S1 = S1[1 : -1]
    S1 = S1.replace('(', ',')
    SS = ''
    for i in range(len(S1) - 1):
        SS += S1[i]
        if not check(S1[i]) and check(S1[i + 1]):
            SS += '('
    SS += S1[len(S1) - 1]
    if check(S1[0]):
        SS = '(' + SS
    S1 = '(1, ' + SS + ')'
    S1 = S1.replace(')(', '),(')
    S1 = S1.replace(')"', '),"')
    S1 = S1.replace('"(', '",(')
    hoge = eval(S1)
    ans = 0
    m = {}
    def func(obj):
        if type(obj) == type("hoge"):
            m[obj] = len(obj)
            return len(obj)
        num = obj[0]
        ret = 0
        for i in range(1, len(obj)):
            ret += num * func(obj[i])
        m[obj] = ret
        return ret

    def func2(obj, index):
        if type(obj) == type("hoge"):
            return obj[index]
        num = obj[0]
        S = m[obj]
        index %= S / num
        ret = 0
        for i in range(1, len(obj)):
            ret += m[obj[i]]
            if ret > index:
                ret -= m[obj[i]]
                return func2(obj[i], index - ret)
        return '0'
    
    func(hoge)
    if N >= m[hoge]:
        print '0'
    else:
        print func2(hoge, N)