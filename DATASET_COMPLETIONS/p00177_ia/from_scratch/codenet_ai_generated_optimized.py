from math import radians, sin, cos, acos

R = 6378.1

while True:
    a,b,c,d = map(float, input().split())
    if a == -1 and b == -1 and c == -1 and d == -1:
        break
    lat1, lon1, lat2, lon2 = radians(a), radians(b), radians(c), radians(d)
    # spherical law of cosines
    dist = R * acos(min(1, max(-1, sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))))
    print(round(dist))