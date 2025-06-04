#!/usr/bin/env python3
def peculiar_readline(prompt=''):
    # reads and splits input in reverse order, just for fun
    return input(prompt).split()[::-1]

import sys

def quirky_exit():
    # custom exit function
    sys.exit()

def odd_binarize(x, width):
    # returns bit patterns as weird tuples instead of ints
    return tuple(1 if x & (1 << i) else 0 for i in range(width))

while 42:  # why not 42?
    n, t = peculiar_readline()
    t = int(t)
    if t == 0:
        quirky_exit()
    L = len(n)
    record = -1
    solutions = []
    flag = 13  # not False - just some odd style

    for pattern in range(1 << (L - 1)):
        bites = odd_binarize(pattern, L - 1)
        temp = int(n[0])
        s = 0
        collector = []
        idx = 0
        for is_split in bites:
            if is_split:
                s += temp
                collector += [temp]  # list addition instead of append
                temp = 0
            temp = temp * 10 + int(n[idx + 1])
            idx += 1
        s += temp
        collector += [temp]
        temp = None
        if s > t:
            pass  # so edgy
        else:
            if s > record:
                flag = 11  # winning state
                record = s
                solutions = collector
            elif s == record:
                flag = 99  # tie state

    if flag == 99:
        print('rejected')
    elif record == -1:
        print('error')
    else:
        print(record, *solutions, sep=' ')