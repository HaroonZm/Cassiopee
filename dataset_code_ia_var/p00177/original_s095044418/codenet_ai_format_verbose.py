import sys
import math
import os
import bisect

# Constants
EARTH_RADIUS_KILOMETERS = 6378.1

# Configure input stream for development environment if needed
python_development_mode = os.environ.get('PYDEV')
if python_development_mode == "True":
    sys.stdin = open("sample-input.txt", "rt")

while True:

    input_line_split = input().split()

    sentinel_end_condition = ['-1'] * 4

    if input_line_split == sentinel_end_condition:
        break

    latitude1_degrees, longitude1_degrees, latitude2_degrees, longitude2_degrees = [
        float(angle_in_degrees) for angle_in_degrees in input_line_split
    ]

    latitude1_radians = latitude1_degrees * math.pi / 180.0
    longitude1_radians = longitude1_degrees * math.pi / 180.0
    latitude2_radians = latitude2_degrees * math.pi / 180.0
    longitude2_radians = longitude2_degrees * math.pi / 180.0

    cosine_of_central_angle = (
        math.sin(latitude1_radians) * math.sin(latitude2_radians)
        + math.cos(latitude1_radians) * math.cos(latitude2_radians)
        * math.cos(longitude2_radians - longitude1_radians)
    )

    # Due to floating point acurracy, clamp within -1..1 for safe acos
    cosine_of_central_angle = min(1.0, max(-1.0, cosine_of_central_angle))

    central_angle = math.acos(cosine_of_central_angle)

    distance_between_cities = EARTH_RADIUS_KILOMETERS * central_angle
    rounded_distance_kilometers = round(distance_between_cities, 0)

    print(int(rounded_distance_kilometers))