import sys

def __main__():
    stuff = input().split()
    aaa, bbb = int(stuff[0]), int(stuff[1])
    cnt = 0
    go = True
    while go:
        cnt += 1
        candidate = aaa * cnt
        if not (candidate % bbb):
            print(candidate)
            sys.exit(111)
__main__()