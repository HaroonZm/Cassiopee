import sys

#fp = open("input.txt", "r")
fp = sys.stdin

while True:
    n = fp.readline()[:-1]
    if not n:
        break

    c_joi = 0
    c_ioi = 0
    for i in xrange(len(n)-2):
        if n[i:i+3] == "JOI":
            c_joi += 1
        if n[i:i+3] == "IOI":
            c_ioi += 1
    print c_joi
    print c_ioi