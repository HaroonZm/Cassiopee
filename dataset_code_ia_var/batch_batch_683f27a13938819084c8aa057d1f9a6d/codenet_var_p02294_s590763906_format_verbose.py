import math

EPSILON = 1e-10

# **************************** Classes ****************************

class Point:

    def __init__(self, coordinate_x, coordinate_y):
        self.x = coordinate_x
        self.y = coordinate_y

    def __sub__(self, other_point):
        return Point(self.x - other_point.x, self.y - other_point.y)

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def __mul__(self, scalar_value):
        return Point(self.x * scalar_value, self.y * scalar_value)

    def __truediv__(self, scalar_value):
        return Point(self.x / scalar_value, self.y / scalar_value)

    def __str__(self):
        return f"{self.x},{self.y}"

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __lt__(self, other_point):
        if abs(self.y - other_point.y) < EPSILON:
            return self.x < other_point.x
        else:
            return self.y < other_point.y

    def __eq__(self, other_point):
        return (abs(self.x - other_point.x) < EPSILON) and (abs(self.y - other_point.y) < EPSILON)


class Segment:

    def __init__(self, endpoint_start, endpoint_end):
        self.p1 = endpoint_start
        self.p2 = endpoint_end

    def __str__(self):
        return f"Segment:({self.p1};{self.p2})"

    def __repr__(self):
        return f"Segment:({self.p1};{self.p2})"


class Circle:

    def __init__(self, center_point, radius_value):
        self.center = center_point
        self.radius = radius_value

    def __str__(self):
        return f"Circle:(center point: {self.center}; radius: {self.radius})"

    def __repr__(self):
        return f"Circle:(center point: {self.center}; radius: {self.radius})"


class Polygon:

    def __init__(self, points_list=None):
        if points_list is None:
            points_list = []
        self.vertices = points_list
        self.vertex_count = len(points_list)

    def __getitem__(self, index):
        return self.vertices[index]

    def __setitem__(self, index, point):
        self.vertices[index] = point

    def __iter__(self):
        return iter(self.vertices)

    def add_vertex(self, index, point):
        self.vertices.insert(index, point)
        self.vertex_count += 1

    def remove_vertex(self, index):
        self.vertex_count -= 1
        return self.vertices.pop(index)

    def sort_by_y_then_x(self):
        self.vertices.sort()

    def __str__(self):
        return f"Polygon:{tuple(self.vertices)}"

    def __repr__(self):
        return f"Polygon:{tuple(self.vertices)}"

    def __len__(self):
        return len(self.vertices)

    def __eq__(self, other_polygon):
        return self.vertices == other_polygon.vertices

    def draw(self):
        import turtle
        turtle.screensize(800, 800, "black")
        turtle.title("Polygon convex hull")
        turtle.setworldcoordinates(-400, -400, 400, 400)
        t = turtle.Turtle()
        t.pencolor("red")
        for vertex in self.vertices:
            t.goto(vertex.x, vertex.y)
            t.dot(10, 'white')


# **************************** Vector Operations ****************************

def squared_magnitude(vector_point):
    return vector_point.x * vector_point.x + vector_point.y * vector_point.y

def vector_length(vector_point):
    return math.sqrt(vector_point.x * vector_point.x + vector_point.y * vector_point.y)

def dot_product(vector_a, vector_b):
    return vector_a.x * vector_b.x + vector_a.y * vector_b.y

def cross_product(vector_a, vector_b):
    return vector_a.x * vector_b.y - vector_a.y * vector_b.x

def project_point_onto_segment(segment, point):
    segment_direction = segment.p2 - segment.p1
    projection_factor = dot_product(point - segment.p1, segment_direction) / squared_magnitude(segment_direction)
    return segment.p1 + segment_direction * projection_factor

def distance_between_points(point_a, point_b):
    return vector_length(point_a - point_b)

def distance_from_point_to_line(line_segment, point):
    return abs(cross_product(line_segment.p2 - line_segment.p1, point - line_segment.p1) / vector_length(line_segment.p2 - line_segment.p1))

def distance_from_point_to_segment(segment, point):
    if dot_product(segment.p2 - segment.p1, point - segment.p1) < 0.0:
        return vector_length(point - segment.p1)
    if dot_product(segment.p1 - segment.p2, point - segment.p2) < 0.0:
        return vector_length(point - segment.p2)
    return distance_from_point_to_line(segment, point)

def are_segments_orthogonal(segment1, segment2):
    return abs(dot_product(segment1.p2 - segment1.p1, segment2.p2 - segment2.p1)) < EPSILON

def are_segments_parallel(segment1, segment2):
    return abs(cross_product(segment1.p2 - segment1.p1, segment2.p2 - segment2.p1)) < EPSILON

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = -2
ONLINE_FRONT = 2
ON_SEGMENT = 0

def determine_orientation(center_point, point1, point2):
    vector_a = point1 - center_point
    vector_b = point2 - center_point
    cross_val = cross_product(vector_a, vector_b)

    if cross_val > EPSILON:
        return COUNTER_CLOCKWISE
    if cross_val < -EPSILON:
        return CLOCKWISE
    if dot_product(vector_a, vector_b) < -EPSILON:
        return ONLINE_BACK
    if squared_magnitude(vector_a) < squared_magnitude(vector_b):
        return ONLINE_FRONT
    return ON_SEGMENT

def left_turn_test(reference_point, first_point, second_point):
    vector_a = first_point - reference_point
    vector_b = second_point - reference_point
    cross_val = cross_product(vector_a, vector_b)

    if cross_val > EPSILON:
        return 1
    elif abs(cross_val) < EPSILON and squared_magnitude(vector_a) <= squared_magnitude(vector_b):
        return 2  # Collinear, second_point is on the extension of reference_point->first_point
    elif abs(cross_val) < EPSILON and squared_magnitude(vector_a) > squared_magnitude(vector_b):
        return -2  # Collinear, second_point is on the opposite extension
    else:
        return -1

def symmetric_point_across_segment(axis_segment, external_point):
    projection = project_point_onto_segment(axis_segment, external_point)
    return external_point + (projection - external_point) * 2.0

def do_segments_intersect(segment1, segment2):
    return do_two_segments_intersect(segment1.p1, segment1.p2, segment2.p1, segment2.p2)

def distance_between_segments(segment1, segment2):
    if do_segments_intersect(segment1, segment2):
        return 0.0
    return min(
        distance_from_point_to_segment(segment1, segment2.p1),
        distance_from_point_to_segment(segment1, segment2.p2),
        distance_from_point_to_segment(segment2, segment1.p1),
        distance_from_point_to_segment(segment2, segment1.p2)
    )

def do_two_segments_intersect(point1, point2, point3, point4):
    return (determine_orientation(point1, point2, point3) * determine_orientation(point1, point2, point4) <= 0
            and determine_orientation(point3, point4, point1) * determine_orientation(point3, point4, point2) <= 0)


# **************************** Segment Intersection Query Logic ****************************

number_of_queries = int(input())

for query_index in range(number_of_queries):
    input_values = [int(token_value) for token_value in input().split()]
    segment1_start = Point(input_values[0], input_values[1])
    segment1_end = Point(input_values[2], input_values[3])
    segment2_start = Point(input_values[4], input_values[5])
    segment2_end = Point(input_values[6], input_values[7])

    are_endpoints_shared = (
        segment1_start == segment2_start or
        segment1_start == segment2_end or
        segment1_end == segment2_start or
        segment1_end == segment2_end
    )

    cross_product_1 = cross_product(segment1_end - segment1_start, segment2_start - segment1_start)
    cross_product_2 = cross_product(segment1_end - segment1_start, segment2_end - segment1_start)
    cross_product_3 = cross_product(segment2_end - segment2_start, segment1_start - segment2_start)
    cross_product_4 = cross_product(segment2_end - segment2_start, segment1_end - segment2_start)

    if are_endpoints_shared:
        print(1)
    elif cross_product_1 * cross_product_2 < 0 and cross_product_3 * cross_product_4 < 0:
        print(1)
    elif abs(cross_product_1) < EPSILON and dot_product(segment1_end - segment1_start, segment2_start - segment1_start) > 0 and \
         vector_length(segment2_start - segment1_start) < vector_length(segment1_end - segment1_start):
        print(1)
    elif abs(cross_product_2) < EPSILON and dot_product(segment1_end - segment1_start, segment2_end - segment1_start) > 0 and \
         vector_length(segment2_end - segment1_start) < vector_length(segment1_end - segment1_start):
        print(1)
    elif abs(cross_product_3) < EPSILON and dot_product(segment2_end - segment2_start, segment1_start - segment2_start) > 0 and \
         vector_length(segment1_start - segment2_start) < vector_length(segment2_end - segment2_start):
        print(1)
    elif abs(cross_product_4) < EPSILON and dot_product(segment2_end - segment2_start, segment1_end - segment2_start) > 0 and \
         vector_length(segment1_end - segment2_start) < vector_length(segment2_end - segment2_start):
        print(1)
    else:
        print(0)