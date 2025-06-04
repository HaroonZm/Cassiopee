from math import acos, sin, cos, radians

while True:
    latitude_city1_deg, longitude_city1_deg, latitude_city2_deg, longitude_city2_deg = map(float, input().split())

    if latitude_city1_deg == longitude_city1_deg == latitude_city2_deg == longitude_city2_deg == -1:
        break

    latitude_city1_rad = radians(latitude_city1_deg)
    longitude_city1_rad = radians(longitude_city1_deg)
    latitude_city2_rad = radians(latitude_city2_deg)
    longitude_city2_rad = radians(longitude_city2_deg)

    earth_radius_km = 6378.1

    central_angle = acos(
        sin(latitude_city1_rad) * sin(latitude_city2_rad) +
        cos(latitude_city1_rad) * cos(latitude_city2_rad) * cos(longitude_city2_rad - longitude_city1_rad)
    )

    distance_kilometers = earth_radius_km * central_angle

    distance_kilometers_rounded = int(distance_kilometers + 0.5)

    print(distance_kilometers_rounded)