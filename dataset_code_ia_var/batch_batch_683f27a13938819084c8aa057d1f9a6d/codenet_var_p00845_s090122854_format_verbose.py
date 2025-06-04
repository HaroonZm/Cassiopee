import math

while True:
    
    number_of_stars = int(input())
    
    if number_of_stars == 0:
        break

    star_coordinates_list = [
        list(map(float, input().split()))
        for _ in range(number_of_stars)
    ]
    
    star_is_visible = [False for _ in range(number_of_stars)]
    
    number_of_telescopic_scopes = int(input())
    
    telescope_scopes_parameters = [
        list(map(float, input().split()))
        for _ in range(number_of_telescopic_scopes)
    ]
    
    for telescope_scope in telescope_scopes_parameters:
        
        telescope_position_vector_length = (
            telescope_scope[0] ** 2 +
            telescope_scope[1] ** 2 +
            telescope_scope[2] ** 2
        ) ** 0.5
        
        telescope_scope_angle = telescope_scope[3]

        for star_index in range(len(star_coordinates_list)):
            
            star_coordinates = star_coordinates_list[star_index]
            
            star_position_vector_length = (
                star_coordinates[0] ** 2 +
                star_coordinates[1] ** 2 +
                star_coordinates[2] ** 2
            ) ** 0.5

            dot_product = (
                telescope_scope[0] * star_coordinates[0] +
                telescope_scope[1] * star_coordinates[1] +
                telescope_scope[2] * star_coordinates[2]
            )

            cos_angle_product = (
                math.cos(telescope_scope_angle) *
                telescope_position_vector_length *
                star_position_vector_length
            )

            if cos_angle_product < dot_product:
                star_is_visible[star_index] = True

    number_of_visible_stars = sum(star_is_visible)
    
    print(number_of_visible_stars)