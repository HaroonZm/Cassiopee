import sys

for line in sys.stdin:
    l = line.split(',')
    uid = l[0]
    w = float(l[1])
    h = float(l[2])
    if w / (h * h) >= 25:
        print(uid)