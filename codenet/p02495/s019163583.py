from __future__ import print_function

while 1:
    h, w = map(int, raw_input().split())
    turn = 1
    if h == w == 0:
        break
    for i in range(h):
        for j in range(w):
            print('#' if turn ^ (j % 2) else '.', sep='', end='')
        print()
        turn ^= 1
    print()