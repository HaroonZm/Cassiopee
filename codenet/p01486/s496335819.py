#!/usr/bin/env python

S = raw_input()

S = S.replace('mew', '[1]')
S = S.replace('me', 'm[1]e')
S = S.replace('ew', 'e[1]w')
S = S.replace('m', '[')
S = S.replace('e', ',')
S = S.replace('w', ']')

for i in range(500):
    S = S.replace('[[1],[1]]', '[1]')

if S == '[1]' or S == '':
    print 'Cat'
else:
    print 'Rabbit'