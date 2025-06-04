import sys
import math
import os
import bisect

ENV_PYDEV_FLAG = os.environ.get('PYDEV')
if ENV_PYDEV_FLAG == "True":
    sys.stdin = open("sample-input.txt", "rt")

EARTH_RADIUS_KM = 6378.1

while True:
    input_values = input().split()
    if input_values == ['-1'] * 4:
        break
    latitude1_rad, longitude1_rad, latitude2_rad, longitude2_rad = [float(degree) * math.pi / 180.0 for degree in input_values]
    spherical_distance = math.acos(
        math.sin(latitude1_rad) * math.sin(latitude2_rad) +
        math.cos(latitude1_rad) * math.cos(latitude2_rad) * math.cos(longitude2_rad - longitude1_rad)
    )
    distance_km_rounded = round(EARTH_RADIUS_KM * spherical_distance, 0)
    print(int(distance_km_rounded))