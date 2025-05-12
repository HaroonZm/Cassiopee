#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

m = {}
m2 = {}

def check(S):
    return ord('0') <= ord(S) and ord(S) <= ord('9')

while True:
    S = raw_input()
    if S == 'END_OF_FIRST_PART':
        break
    atom, w = S.split()
    if len(atom) >= 2:
        m2[atom] = w
    else:
        m[atom] = w

while True:
    S = raw_input()
    if S == '0':
        break
    SS = ''
    for i in range(len(S) - 1):
        SS += S[i]
        if not check(S[i]) and check(S[i + 1]):
            SS += '*'
        if check(S[i]) and not check(S[i + 1]):
            SS += '+'
    SS += S[-1]
    S = '(' + SS + ')'
    for atom in m2:
        S = S.replace(atom, m2[atom] + '+')
    for atom in m:
        S = S.replace(atom, m[atom] + '+')
    S = S.replace('+*', '*')
    S = S.replace('+)', ')')
    try:
        ret = eval(S)
    except:
        ret = "UNKNOWN"
    print ret