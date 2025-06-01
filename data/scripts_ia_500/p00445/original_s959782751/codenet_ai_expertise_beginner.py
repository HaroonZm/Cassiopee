import sys

fp = sys.stdin

while True:
    n = fp.readline()
    if not n:
        break
    n = n.strip()

    count_joi = 0
    count_ioi = 0
    length = len(n)
    for i in range(length - 2):
        triplet = n[i:i+3]
        if triplet == "JOI":
            count_joi += 1
        if triplet == "IOI":
            count_ioi += 1

    print(count_joi)
    print(count_ioi)