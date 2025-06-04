import math

CONSTANT_PI = 3.1415926535897932384626433832795
CONSTANT_DEG_TO_RAD = CONSTANT_PI / 180.0
CONSTANT_EARTH_RADIUS_KM = 6378.1

def compute_distance_between_coordinates(lat1_deg, lon1_deg, lat2_deg, lon2_deg):
    lat1_rad = lat1_deg * CONSTANT_DEG_TO_RAD
    lon1_rad = lon1_deg * CONSTANT_DEG_TO_RAD
    lat2_rad = lat2_deg * CONSTANT_DEG_TO_RAD
    lon2_rad = lon2_deg * CONSTANT_DEG_TO_RAD
    cos_term = math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(lon1_rad - lon2_rad)
    sin_term = math.sin(lat1_rad) * math.sin(lat2_rad)
    angular_distance = math.acos(cos_term + sin_term)
    distance = CONSTANT_EARTH_RADIUS_KM * angular_distance
    return int(distance + 0.5)

def main():
    while True:
        input_values = list(map(float, input().split()))
        latitude1, longitude1, latitude2, longitude2 = input_values
        if (latitude1, longitude1, latitude2, longitude2) == (-1.0, -1.0, -1.0, -1.0):
            break
        result_distance = compute_distance_between_coordinates(latitude1, longitude1, latitude2, longitude2)
        print(result_distance)

if __name__ == "__main__":
    main()