import math

def calculate_cosine_similarity(star_coordinates, telescope_direction_vector):
    dot_product = sum([star_component * telescope_component for star_component, telescope_component in zip(star_coordinates, telescope_direction_vector)])
    
    star_magnitude = (sum(component ** 2 for component in star_coordinates)) ** 0.5
    telescope_vector_magnitude = (sum(component ** 2 for component in telescope_direction_vector)) ** 0.5
    
    return dot_product / (star_magnitude * telescope_vector_magnitude)


while True:
    number_of_stars = int(input())
    
    if number_of_stars == 0:
        break

    star_coordinates_list = [
        list(map(float, input().split()))
        for _ in range(number_of_stars)
    ]

    number_of_telescopes = int(input())
    
    telescope_parameters_list = [
        list(map(float, input().split()))
        for _ in range(number_of_telescopes)
    ]

    visible_stars_count = 0

    for star_coordinates in star_coordinates_list:
        for telescope_parameters in telescope_parameters_list:
            telescope_direction_vector = telescope_parameters[:-1]
            telescope_angle_radians = telescope_parameters[-1]

            cosine_similarity = calculate_cosine_similarity(
                star_coordinates,
                telescope_direction_vector
            )

            cosine_of_telescope_angle = math.cos(telescope_angle_radians)

            if cosine_of_telescope_angle <= cosine_similarity:
                visible_stars_count += 1
                break

    print(visible_stars_count)