angle_increment_degrees = int(input())

current_angle_degrees = 0

number_of_rotations = 0

while True:
    number_of_rotations += 1

    current_angle_degrees += angle_increment_degrees

    if current_angle_degrees % 360 == 0:
        print(number_of_rotations)
        exit()