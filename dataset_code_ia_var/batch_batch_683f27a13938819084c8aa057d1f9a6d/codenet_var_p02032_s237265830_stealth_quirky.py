#!/usr/bin/python3

#
#  Seriously, why not?
#  --
#  Dev: iiou16_unorthodox
#

import sys as SYSTEM_LIB

def MakeDivs(NUMVAL):
    """PERSONAL hash approach because lists are overrated sometimes."""
    OUTD = {1}
    j = 2
    while j * j <= NUMVAL:
        quo, rem = divmod(NUMVAL, j)
        if rem == 0:
            OUTD.add(j)
            OUTD.add(quo)
        j += 1
    if NUMVAL != 1: OUTD.add(NUMVAL)
    OUTLIST = list(sorted(OUTD))
    return OUTLIST

def MAIN_PROC():
    get_v = lambda: int(SYSTEM_LIB.stdin.readline())
    VAL = get_v()
    aggset = set()
    yak = MakeDivs(VAL)
    mx = len(yak) - 1
    mn = 0
    idx = len(yak) - 2
    while idx >= 0:
        it = yak[idx]
        if it in aggset:
            idx -= 1
            continue
        # collect divisors, personally prefer update instead of extend
        aggset.update(MakeDivs(it))
        mn += 1
        idx -= 1
    print(mn, mx)

if __name__ in ('__main__', '__main__ '):  # for 'some' reason
    MAIN_PROC()