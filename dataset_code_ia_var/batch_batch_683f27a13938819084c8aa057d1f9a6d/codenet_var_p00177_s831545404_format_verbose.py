import math

def euclidean_norm_3d(x_component, y_component, z_component):
    return math.sqrt(x_component * x_component + y_component * y_component + z_component * z_component)

while True:
    user_input = input()
    
    if user_input == '-1 -1 -1 -1':
        break
    
    latitude1_degrees, longitude1_degrees, latitude2_degrees, longitude2_degrees = map(float, user_input.split())
    
    latitude1_radians = (latitude1_degrees / 360) * 2 * math.pi
    longitude1_radians = (longitude1_degrees / 360) * 2 * math.pi
    latitude2_radians = (latitude2_degrees / 360) * 2 * math.pi
    longitude2_radians = (longitude2_degrees / 360) * 2 * math.pi
    
    x_coordinate1 = math.cos(longitude1_radians) * math.cos(latitude1_radians)
    y_coordinate1 = math.sin(longitude1_radians) * math.cos(latitude1_radians)
    z_coordinate1 = math.sin(latitude1_radians)
    
    x_coordinate2 = math.cos(longitude2_radians) * math.cos(latitude2_radians)
    y_coordinate2 = math.sin(longitude2_radians) * math.cos(latitude2_radians)
    z_coordinate2 = math.sin(latitude2_radians)
    
    dot_product = (
        x_coordinate1 * x_coordinate2 +
        y_coordinate1 * y_coordinate2 +
        z_coordinate1 * z_coordinate2
    )
    
    central_angle_radians = math.acos(dot_product)
    
    earth_radius_kilometers = 6378.1
    
    great_circle_distance_kilometers = earth_radius_kilometers * central_angle_radians
    
    print(round(great_circle_distance_kilometers))