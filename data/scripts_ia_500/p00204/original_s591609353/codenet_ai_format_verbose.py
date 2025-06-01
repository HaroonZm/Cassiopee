import math


class UnidentifiedFlyingObject:
    
    def __init__(self, position_x, position_y, radius, velocity):
        self.distance_from_origin = calculate_distance_from_origin(position_x, position_y)
        self.angle_from_x_axis = calculate_angle_from_x_axis(position_y, position_x)
        self.radius = radius
        self.velocity = velocity


def calculate_distance_from_origin(coordinate_x, coordinate_y):
    return (coordinate_x ** 2 + coordinate_y ** 2) ** 0.5


def calculate_angle_from_x_axis(coordinate_y, coordinate_x):
    angle = math.atan2(coordinate_y, coordinate_x)
    if angle < 0:
        angle += 2 * math.pi
    return angle


def move_ufos_closer_and_remove_if_in_range(ufos_list, boundary_radius):
    ufos_to_remove = []
    for ufo in ufos_list:
        ufo.distance_from_origin -= ufo.velocity
        if ufo.distance_from_origin <= boundary_radius:
            ufos_to_remove.append(ufo)
    for ufo in ufos_to_remove:
        ufos_list.remove(ufo)
    return len(ufos_to_remove)


def check_if_ufo_is_destroyed_by_laser(ufo, laser_angle, boundary_radius):
    angle_difference = abs(ufo.angle_from_x_axis - laser_angle)
    if angle_difference > math.pi:
        angle_difference = 2 * math.pi - angle_difference

    perpendicular_distance = ufo.distance_from_origin * math.sin(angle_difference)
    parallel_distance = ufo.distance_from_origin * math.cos(angle_difference)
    radius_squared = ufo.radius ** 2
    
    if (angle_difference <= math.pi / 2 and perpendicular_distance <= ufo.radius) or (ufo.distance_from_origin <= ufo.radius):
        if parallel_distance + (radius_squared - perpendicular_distance ** 2) ** 0.5 > boundary_radius:
            return True
    return False


def remove_destroyed_ufos_after_shooting(ufos_list, laser_angle, boundary_radius):
    ufos_to_remove = []
    for ufo in ufos_list:
        if check_if_ufo_is_destroyed_by_laser(ufo, laser_angle, boundary_radius):
            ufos_to_remove.append(ufo)
    for ufo in ufos_to_remove:
        ufos_list.remove(ufo)


def main():
    while True:
        boundary_radius, number_of_ufos = map(int, input().split())
        if boundary_radius == 0:
            break

        ufos_list = []
        for _ in range(number_of_ufos):
            position_x, position_y, radius, velocity = map(int, input().split())
            ufos_list.append(UnidentifiedFlyingObject(position_x, position_y, radius, velocity))
        
        total_destroyed_ufos = 0

        while ufos_list:
            total_destroyed_ufos += move_ufos_closer_and_remove_if_in_range(ufos_list, boundary_radius)
            if ufos_list:
                closest_ufo_angle = min(ufos_list, key=lambda ufo: ufo.distance_from_origin).angle_from_x_axis
                remove_destroyed_ufos_after_shooting(ufos_list, closest_ufo_angle, boundary_radius)

        print(total_destroyed_ufos)


main()