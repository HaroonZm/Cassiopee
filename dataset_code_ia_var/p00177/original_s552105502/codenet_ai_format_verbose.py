import math

PI_VALUE = 3.1415926535897932384626433832795
DEGREE_TO_RADIAN = PI_VALUE / 180.0
EARTH_RADIUS_KM = 6378.1

while True:
    latitude_city1_degrees, longitude_city1_degrees, latitude_city2_degrees, longitude_city2_degrees = map(float, input().split())

    if (longitude_city1_degrees == -1 and latitude_city1_degrees == -1 and
        longitude_city2_degrees == -1 and latitude_city2_degrees == -1):
        break

    latitude_city1_radians = latitude_city1_degrees * DEGREE_TO_RADIAN
    latitude_city2_radians = latitude_city2_degrees * DEGREE_TO_RADIAN
    longitude_difference_radians = (longitude_city1_degrees - longitude_city2_degrees) * DEGREE_TO_RADIAN

    cosine_of_central_angle = (math.cos(latitude_city1_radians) * math.cos(latitude_city2_radians) * math.cos(longitude_difference_radians) +
                              math.sin(latitude_city1_radians) * math.sin(latitude_city2_radians))

    central_angle = math.acos(cosine_of_central_angle)

    distance_between_cities_km = EARTH_RADIUS_KM * central_angle

    distance_between_cities_km_rounded = int(distance_between_cities_km + 0.5)

    print(distance_between_cities_km_rounded)