from math import cos as cosine_radians
from math import sin as sine_radians
from math import sqrt
from math import radians

def cosine_degrees(angle_in_degrees):
    return cosine_radians(radians(angle_in_degrees))

def sine_degrees(angle_in_degrees):
    return sine_radians(radians(angle_in_degrees))

def generate_five_pointed_star_vertices(center_x, center_y, orientation_angle_deg, radius):
    star_vertices = []
    for vertex_index in range(5):
        angle = orientation_angle_deg - 72 * vertex_index * 2
        vertex_x = center_x - radius * sine_degrees(angle)
        vertex_y = center_y + radius * cosine_degrees(angle)
        star_vertices.append((vertex_x, vertex_y))
    # Close the loop by repeating the first vertex at the end
    star_vertices.append(star_vertices[0])
    return star_vertices

def minimum_distance_between_two_line_segments(segment1_point1, segment1_point2, segment2_point1, segment2_point2):
    # Check if the segments intersect
    det1 = ((segment1_point2[0] - segment1_point1[0]) * (segment2_point1[1] - segment1_point1[1]) -
            (segment1_point2[1] - segment1_point1[1]) * (segment2_point1[0] - segment1_point1[0]))
    det2 = ((segment1_point2[0] - segment1_point1[0]) * (segment2_point2[1] - segment1_point1[1]) -
            (segment1_point2[1] - segment1_point1[1]) * (segment2_point2[0] - segment1_point1[0]))
    det3 = ((segment2_point2[0] - segment2_point1[0]) * (segment1_point1[1] - segment2_point1[1]) -
            (segment2_point2[1] - segment2_point1[1]) * (segment1_point1[0] - segment2_point1[0]))
    det4 = ((segment2_point2[0] - segment2_point1[0]) * (segment1_point2[1] - segment2_point1[1]) -
            (segment2_point2[1] - segment2_point1[1]) * (segment1_point2[0] - segment2_point1[0]))
    if (det1 * det2 <= 0) and (det3 * det4 <= 0):
        return 0

    vector1_x = segment1_point2[0] - segment1_point1[0]
    vector1_y = segment1_point2[1] - segment1_point1[1]
    segment1_length_squared = vector1_x ** 2 + vector1_y ** 2

    # Distance from segment2_point1 to segment1
    projection1 = (vector1_x * (segment2_point1[0] - segment1_point1[0]) +
                   vector1_y * (segment2_point1[1] - segment1_point1[1]))
    if 0 <= projection1 <= segment1_length_squared:
        numerator = abs(vector1_x * (segment2_point1[1] - segment1_point1[1]) -
                        vector1_y * (segment2_point1[0] - segment1_point1[0]))
        denominator = sqrt(segment1_length_squared)
        distance_to_segment2_point1 = numerator / denominator
    else:
        distance_to_segment2_point1 = min(
            sqrt((segment2_point1[0] - segment1_point1[0]) ** 2 + (segment2_point1[1] - segment1_point1[1]) ** 2),
            sqrt((segment2_point1[0] - segment1_point2[0]) ** 2 + (segment2_point1[1] - segment1_point2[1]) ** 2)
        )

    # Distance from segment2_point2 to segment1
    projection2 = (vector1_x * (segment2_point2[0] - segment1_point1[0]) +
                   vector1_y * (segment2_point2[1] - segment1_point1[1]))
    if 0 <= projection2 <= segment1_length_squared:
        numerator = abs(vector1_x * (segment2_point2[1] - segment1_point1[1]) -
                        vector1_y * (segment2_point2[0] - segment1_point1[0]))
        denominator = sqrt(segment1_length_squared)
        distance_to_segment2_point2 = numerator / denominator
    else:
        distance_to_segment2_point2 = min(
            sqrt((segment2_point2[0] - segment1_point1[0]) ** 2 + (segment2_point2[1] - segment1_point1[1]) ** 2),
            sqrt((segment2_point2[0] - segment1_point2[0]) ** 2 + (segment2_point2[1] - segment1_point2[1]) ** 2)
        )
    return min(distance_to_segment2_point1, distance_to_segment2_point2)

def minimum_distance_between_two_five_pointed_stars(
    star1_center_x, star1_center_y, star1_orientation_deg, star1_radius,
    star2_center_x, star2_center_y, star2_orientation_deg, star2_radius
):
    star1_vertices = generate_five_pointed_star_vertices(
        star1_center_x, star1_center_y, star1_orientation_deg, star1_radius
    )
    star2_vertices = generate_five_pointed_star_vertices(
        star2_center_x, star2_center_y, star2_orientation_deg, star2_radius
    )
    minimum_distance = float('inf')
    for star1_index in range(5):
        for star2_index in range(5):
            distance1 = minimum_distance_between_two_line_segments(
                star1_vertices[star1_index], star1_vertices[star1_index + 1],
                star2_vertices[star2_index], star2_vertices[star2_index + 1]
            )
            distance2 = minimum_distance_between_two_line_segments(
                star2_vertices[star2_index], star2_vertices[star2_index + 1],
                star1_vertices[star1_index], star1_vertices[star1_index + 1]
            )
            minimum_distance = min(minimum_distance, distance1, distance2)
    return minimum_distance

number_of_stars, start_star_index, end_star_index = map(int, input().split())

while number_of_stars != 0:
    star_parameters_list = []
    for star_index in range(number_of_stars):
        center_x, center_y, orientation_deg, radius = map(int, input().split())
        star_parameters_list.append((center_x, center_y, orientation_deg, radius))

    minimum_distances_between_stars = [
        [0] * number_of_stars for _ in range(number_of_stars)
    ]

    for star_index1 in range(number_of_stars):
        center_x1, center_y1, orientation_deg1, radius1 = star_parameters_list[star_index1]
        for star_index2 in range(star_index1 + 1, number_of_stars):
            center_x2, center_y2, orientation_deg2, radius2 = star_parameters_list[star_index2]
            minimum_distance = minimum_distance_between_two_five_pointed_stars(
                center_x1, center_y1, orientation_deg1, radius1,
                center_x2, center_y2, orientation_deg2, radius2
            )
            minimum_distances_between_stars[star_index1][star_index2] = minimum_distance

    for star_index1 in range(number_of_stars):
        for star_index2 in range(star_index1):
            minimum_distances_between_stars[star_index1][star_index2] = minimum_distances_between_stars[star_index2][star_index1]

    # Floyd-Warshall algorithm to compute all-pairs shortest paths
    for intermediate_star in range(number_of_stars):
        for source_star in range(number_of_stars):
            for destination_star in range(number_of_stars):
                new_distance = (minimum_distances_between_stars[source_star][intermediate_star] +
                                minimum_distances_between_stars[intermediate_star][destination_star])
                if new_distance < minimum_distances_between_stars[source_star][destination_star]:
                    minimum_distances_between_stars[source_star][destination_star] = new_distance

    print(
        minimum_distances_between_stars[start_star_index - 1][end_star_index - 1]
    )
    number_of_stars, start_star_index, end_star_index = map(int, input().split())