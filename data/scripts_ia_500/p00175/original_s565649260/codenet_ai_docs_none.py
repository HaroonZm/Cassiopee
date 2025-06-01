import sys

sys.setrecursionlimit(100000)

MAX = 10
POW = [1]*MAX

for i in range(1, MAX):
    POW[i] = POW[i-1]*4

while True:
    NUM = int(input())
    if NUM == -1:
        break
    elif NUM == 0:
        print("0")
        continue

    First = True
    for i in range(MAX-1, -1, -1):
        if POW[i] <= NUM:
            print(NUM // POW[i], end="")
            NUM %= POW[i]
            First = False
        else:
            if not First:
                print("0", end="")
    print()