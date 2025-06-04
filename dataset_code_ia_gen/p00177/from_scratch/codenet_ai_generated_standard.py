import math
R = 6378.1
while True:
    a,b,c,d = map(float, input().split())
    if a == b == c == d == -1:
        break
    lat1 = math.radians(a)
    lon1 = math.radians(b)
    lat2 = math.radians(c)
    lon2 = math.radians(d)
    delta_sigma = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon1 - lon2))
    dist = R * delta_sigma
    print(round(dist))