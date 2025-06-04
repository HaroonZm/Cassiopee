from math import acos as fn_acos, sin as fn_sin, cos as fn_cos, radians as fn_radians

while True:
    lat1_deg, lon1_deg, lat2_deg, lon2_deg = map(float, input().split())
    if lat1_deg == lon1_deg == lat2_deg == lon2_deg == -1:
        break
    lat1_rad = fn_radians(lat1_deg)
    lat2_rad = fn_radians(lat2_deg)
    lon1_rad = fn_radians(lon1_deg)
    lon2_rad = fn_radians(lon2_deg)
    delta_lon_rad = lon2_rad - lon1_rad
    central_angle = fn_acos(fn_sin(lat1_rad) * fn_sin(lat2_rad) + fn_cos(lat1_rad) * fn_cos(lat2_rad) * fn_cos(delta_lon_rad))
    earth_radius_km = 6378.1
    distance_km = earth_radius_km * central_angle
    print(int(distance_km + 0.5))