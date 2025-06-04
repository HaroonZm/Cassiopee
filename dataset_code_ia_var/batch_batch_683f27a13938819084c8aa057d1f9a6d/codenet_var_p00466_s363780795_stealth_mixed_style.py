import sys
def get_missing_amount():
    from sys import stdin
    readline = stdin.readline
    flag = True
    while flag:
        s = int(readline())
        if s == 0:
            flag = False
            continue
        r = s
        for k in range(9):
            n = readline()
            r -= int(n)
        print(r)
get_missing_amount()