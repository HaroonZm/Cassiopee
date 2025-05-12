# Aizu Problem 0177: Distance Between Two Cities
#
import sys, math, os, bisect

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

R = 6378.1
while True:
    inp = input().split()
    if inp == ['-1'] * 4:
        break
    lat1, long1, lat2, long2 = [float(_) * math.pi / 180. for _ in inp]
    dist = round(R * math.acos(math.sin(lat1)*math.sin(lat2) + \
                               math.cos(lat1)*math.cos(lat2)*math.cos(long2-long1)), 0)
    print(int(dist))