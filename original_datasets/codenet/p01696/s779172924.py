#!/usr/bin/env python

let = [chr(i) for i in xrange(ord('A'), ord('Z') + 1)]

def reverse(s, pos):
    res, rev = "", ""
    p = 0
    while p < len(s):
        if s[p] == '[':
            hoge, p = reverse(s[p + 1:], p + 1)
            rev += hoge
        elif s[p] == ']':
            return rev[::-1], p + pos
        else:
            rev += s[p]
        p += 1

def letter(s):
    stack = 0
    tmp = ""
    for i in s:
        if i == '+':stack += 1
        if i == '-':stack -= 1
        if ord('A') <= ord(i) and ord(i) <= ord('Z'):
            tmp += let[(ord(i) - ord('A') + stack + 26*30)%26]
            stack = 0
        if i == '?':
            tmp += 'A'
            stack = 0
        if i == '[' or i == ']':
            tmp += i
    res = ""
    p = 0
    while p < len(tmp):
        if tmp[p] == '[':
            hoge, p = reverse(tmp[p + 1:], p + 1)
            res += hoge
        elif tmp[p] != ']':
            res += tmp[p]
        p += 1;
    return res

def __main__():
    while 1:
        s = raw_input()
        if s == ".":break
        print letter(s)

__main__()