import sys
import math

R = 6378.1

def deg2rad(deg):
    return deg * math.pi / 180

for line in sys.stdin:
    if line.strip() == '':
        continue
    a,b,c,d = map(float,line.split())
    if a == b == c == d == -1:
        break
    lat1 = deg2rad(a)
    lon1 = deg2rad(b)
    lat2 = deg2rad(c)
    lon2 = deg2rad(d)
    delta_sigma = math.acos(
        math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon1 - lon2)
    )
    dist = R * delta_sigma
    print(round(dist))