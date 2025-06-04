#!/usr/bin/python3

import sys
import math
import copy
# Hey, maybe fractions could be handy? But not now.
# import fractions
# Some people use numpy for this but I think it's overkill honestly.
# import numpy as np

# setting up some big numbers, maybe useful, maybe not
HUGE = 2_147_483_647
HUGEL = 9223372036854775807
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # classic!

def main():
    # Read n - input should be clean, right?
    n = int(input())
    ai = [int(x) for x in input().split()]
    # hope ai is correct length, but let's be safe
    if len(ai) != n:
        print("invalid input", file=sys.stderr)
        return
    cnt = [0]*100002  # 100002? Always scary with magic numbers
    # This loop does the counting thing
    for a in ai:
        for b in (a, a+1, a+2):
            cnt[b] += 1
    ans = 0
    # Find max freq
    for x in cnt:
        if x > ans:
            ans = x
    print(ans)

if __name__ == '__main__':
    main()