import math

def calc_vector_length_3d(x_val, y_val, z_val):
    return math.sqrt(x_val * x_val + y_val * y_val + z_val * z_val)

def deg_to_rad(deg_val):
    return (deg_val / 360.0) * 2.0 * math.pi

def compute_coords(lon_rad, lat_rad):
    x_coord = math.cos(lat_rad) * math.cos(lon_rad)
    y_coord = math.sin(lat_rad) * math.cos(lon_rad)
    z_coord = math.sin(lon_rad)
    return x_coord, y_coord, z_coord

def main():
    while True:
        input_str = input()
        if input_str == '-1 -1 -1 -1':
            break
        lon1_deg, lat1_deg, lon2_deg, lat2_deg = map(float, input_str.split())
        lon1_rad = deg_to_rad(lon1_deg)
        lat1_rad = deg_to_rad(lat1_deg)
        lon2_rad = deg_to_rad(lon2_deg)
        lat2_rad = deg_to_rad(lat2_deg)
        x1, y1, z1 = compute_coords(lon1_rad, lat1_rad)
        x2, y2, z2 = compute_coords(lon2_rad, lat2_rad)
        dot_prod = x1 * x2 + y1 * y2 + z1 * z2
        angle_rad = math.acos(dot_prod)
        earth_radius_km = 6378.1
        distance_km = round(earth_radius_km * angle_rad)
        print(distance_km)

main()