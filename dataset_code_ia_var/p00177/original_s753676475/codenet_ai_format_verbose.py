from math import radians, acos, cos, sin

while True:

    user_input = raw_input("Entrez quatre valeurs séparées par des espaces (ou '-1 -1 -1 -1' pour quitter) : ")

    input_values_as_strings = user_input.split()

    input_values_as_floats = list(map(float, input_values_as_strings))

    if input_values_as_floats == [-1.0, -1.0, -1.0, -1.0]:
        break

    latitude_point1_degrees, longitude_point1_degrees, latitude_point2_degrees, longitude_point2_degrees = input_values_as_floats

    latitude_point1_radians = radians(latitude_point1_degrees)
    longitude_point1_radians = radians(longitude_point1_degrees)
    latitude_point2_radians = radians(latitude_point2_degrees)
    longitude_point2_radians = radians(longitude_point2_degrees)

    cosine_of_central_angle = (
        cos(latitude_point1_radians) * cos(latitude_point2_radians) *
        cos(longitude_point1_radians - longitude_point2_radians) +
        sin(latitude_point1_radians) * sin(latitude_point2_radians)
    )

    central_angle = acos(cosine_of_central_angle)

    earth_radius_km = 6378.1

    great_circle_distance_km = int(round(central_angle * earth_radius_km))

    print(great_circle_distance_km)