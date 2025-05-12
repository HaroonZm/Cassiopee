#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

# calculator with "1234567890()+-*/"

# evaluate operation
def operate(term1, term2, op):
    ret = []
    if op == '+':
        for p in it.product(term1, term2):
            ret += [p[0] + p[1]]
    if op == '-':
        for p in it.product(term1, term2):
            ret += [p[0] - p[1]]
    if op == '*':
        for p in it.product(term1, term2):
            ret += [p[0] * p[1]]
    if op == '/':
        for p in it.product(term1, term2):
            if p[1] == 0:
                continue
            if p[0] * p[1] < 0 and p[0] % p[1] != 0:
                ret += [p[0] / p[1] + 1]
            else:
                ret += [p[0] / p[1]]
    return ret

# evaluate expression without bracket
def calc(S):
    if len(S) == 1:
        if type(S[0]) == type(""):
            return [int(S[0])]
        else:
            return S[0]
    ret = []
    for i in range(len(S)):
        if S[i] in ['+', '-', '*', '/']:
            ret += operate(calc(S[:i]), calc(S[i + 1:]), S[i])
    return ret

# evaluate expression
def br(S):
    index = 0
    lst = []
    while True:
        if index >= len(S) or S[index] == ')':
            return index, calc(lst)
        elif S[index] == '(':
            ret, value = br(S[index + 1:])
            index += ret + 1
            lst.append(value)
        else:
            lst.append(S[index])
        index += 1

# "(11+22)" -> ['(', '11', '+', '22', ')']
def split(S):
    ret = ['?']
    c_num = "1234567890"
    for c in S:
        if c in c_num and ret[-1][-1] in c_num:
            ret[-1] += c
        else:
            ret.append(c)
    return ret[1:]

while True:
    S = raw_input()
    if S == '#':
        break
    S = split(S)
    ret = br(S)[1]
    print len(set(ret))