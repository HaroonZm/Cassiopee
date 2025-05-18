#!/usr/bin/env python

left = 'qwertasdfgzxcvb'
while True:
    s = list(input())
    if s[0] == '#':
        break
    t = True if s[0] in left else False
    count = 0
    for c in s:
        if c in left:
            if t!=True:
                t = True
                count += 1
        else:
            if t:
                t = False
                count += 1
    print(count)