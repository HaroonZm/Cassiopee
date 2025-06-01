from sys import stdin
from cmath import phase
from itertools import combinations

def compute_cross_product(complex_point1, complex_point2):
    
    return complex_point1.real * complex_point2.imag - complex_point1.imag * complex_point2.real


def is_counter_clockwise(point1, point2, point3):
    
    vector1 = point2 - point1
    vector2 = point3 - point1
    
    return compute_cross_product(vector1, vector2) > 0


def calculate_signed_triangle_area(point1, point2, point3):
    # Returns the signed area of the triangle formed by three points
    
    vector1 = point2 - point1
    vector2 = point3 - point1
    
    return compute_cross_product(vector1, vector2) / 2


# Reading input data
input_file = stdin

number_of_points = int(input_file.readline())

points_list = []
point_to_id_map = {}

for index in range(1, number_of_points + 1):
    x_coordinate, y_coordinate = map(int, input_file.readline().split())
    complex_point = x_coordinate + y_coordinate * 1j
    points_list.append(complex_point)
    point_to_id_map[complex_point] = index  # Map point to its ID

number_of_queries = int(input_file.readline())
queries_list = [int(input_file.readline()) for _ in range(number_of_queries)]

max_required_polygon_size = max(queries_list) - 2

# Sort points by their imaginary (y) coordinate, then real (x) coordinate for consistency
points_list.sort(key=lambda point: (point.imag, point.real))

# Initialize maximum possible area to a large value based on coordinate constraints
max_possible_area = 20000 * 20000

# Initialize the list to hold minimum areas for polygons of sizes 3 to max_required_polygon_size + 2
minimum_polygon_areas = [max_possible_area for _ in range(max_required_polygon_size)]

# Initialize the list to hold the points forming those minimum area polygons
minimum_area_polygon_points = [None for _ in range(max_required_polygon_size)]


for base_point_index, base_point in enumerate(points_list[:-2], start=1):
    
    # Create a tail list starting from the next point after base_point
    tail_points = points_list[base_point_index:]
    
    # Number of points remaining in the tail
    tail_points_count = number_of_points - base_point_index
    
    # Sort tail points by their angle relative to the base point
    tail_points.sort(key=lambda point: phase(point - base_point))
    
    # Map indices to points in the tail for easier referencing
    index_to_tail_point_map = dict(zip(range(tail_points_count), tail_points))
    
    # Initialize a 2D list (matrix) to store triangle data: area and points forming the triangle
    triangle_record = [[None for _ in range(tail_points_count)] for _ in range(tail_points_count)]
    
    # Generate all possible triangles formed by the base point and two tail points
    for index_j, index_k in combinations(range(tail_points_count), 2):
        
        point_j = index_to_tail_point_map[index_j]
        point_k = index_to_tail_point_map[index_k]
        
        triangle_area = calculate_signed_triangle_area(base_point, point_j, point_k)
        
        triangle_record[index_j][index_k] = [triangle_area, [base_point, point_j, point_k]]
        
        # Update minimum polygon area and points for polygon size 3 if this triangle is smaller
        if triangle_area < minimum_polygon_areas[0]:
            minimum_polygon_areas[0] = triangle_area
            minimum_area_polygon_points[0] = [base_point, point_j, point_k]
    
    # Prepare for constructing convex polygons with more than 3 sides
    previous_dp_state = triangle_record.copy()
    
    current_dp_state = [[None for _ in range(tail_points_count)] for _ in range(tail_points_count)]
    
    for polygon_size_index in range(1, max_required_polygon_size):
        
        # Consider all combinations of three distinct indices for potential polygon expansion
        for index_j, index_k, index_s in combinations(range(tail_points_count), 3):
            
            previous_polygon_info = previous_dp_state[index_j][index_k]
            
            if previous_polygon_info:
                
                point_j = index_to_tail_point_map[index_j]
                point_k = index_to_tail_point_map[index_k]
                point_s = index_to_tail_point_map[index_s]
                
                # Check if points form a counter-clockwise orientation
                if is_counter_clockwise(point_j, point_k, point_s):
                    
                    new_area = previous_polygon_info[0] + triangle_record[index_k][index_s][0]
                    
                    if not current_dp_state[index_k][index_s] or current_dp_state[index_k][index_s][0] > new_area:
                        
                        current_dp_state[index_k][index_s] = [new_area, previous_polygon_info[1] + [point_s]]
                        
                        if new_area < minimum_polygon_areas[polygon_size_index]:
                            minimum_polygon_areas[polygon_size_index] = new_area
                            minimum_area_polygon_points[polygon_size_index] = current_dp_state[index_k][index_s][1]
        
        previous_dp_state = current_dp_state.copy()
        current_dp_state = [[None for _ in range(tail_points_count)] for _ in range(tail_points_count)]


# Output results of queries
for query_size in queries_list:
    
    polygon_points = minimum_area_polygon_points[query_size - 3]
    
    if polygon_points:
        
        # Map complex points back to their original IDs and convert to strings for output
        polygon_point_ids = map(lambda point: str(point_to_id_map[point]), polygon_points)
        
        print(' '.join(polygon_point_ids))
        
    else:
        
        print("NA")