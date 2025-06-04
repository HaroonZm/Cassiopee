from math import radians as deg_to_rad, cos as cos_func, sin as sin_func, acos as acos_func

def get_coordinates():
    return list(map(float, raw_input().split()))

def all_values_termination(coord_list, sentinel_value, count):
    return coord_list == [sentinel_value] * count

def convert_to_radians(coord_list):
    return map(deg_to_rad, coord_list)

def calculate_distance(lat1, lon1, lat2, lon2, earth_radius):
    angle = acos_func(
        cos_func(lat1) * cos_func(lat2) * cos_func(lon1 - lon2) +
        sin_func(lat1) * sin_func(lat2)
    )
    return int(round(angle * earth_radius))

COORD_COUNT = 4
TERMINATION_SENTINEL = -1
EARTH_RADIUS_KM = 6378.1

while True:
    input_coordinates = get_coordinates()
    if all_values_termination(input_coordinates, TERMINATION_SENTINEL, COORD_COUNT):
        break
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = convert_to_radians(input_coordinates)
    distance_km = calculate_distance(lat1_rad, lon1_rad, lat2_rad, lon2_rad, EARTH_RADIUS_KM)
    print distance_km