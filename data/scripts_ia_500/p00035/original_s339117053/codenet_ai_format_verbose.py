import collections


Point = collections.namedtuple("Point", "x y")
Line = collections.namedtuple("Line", "start_point end_point")


def do_lines_intersect(line_a, line_b):
    
    def compute_cross_product_scalar(point_a, point_b, reference_point):
        
        delta_x_a = point_a.x - reference_point.x
        delta_x_b = point_b.x - reference_point.x
        
        delta_y_a = point_a.y - reference_point.y
        delta_y_b = point_b.y - reference_point.y
        
        return (delta_x_a * delta_y_b) - (delta_x_b * delta_y_a)

    cross1 = compute_cross_product_scalar(line_a.start_point, line_a.end_point, line_b.start_point)
    cross2 = compute_cross_product_scalar(line_a.start_point, line_a.end_point, line_b.end_point)

    if not (cross1 > 0) ^ (cross2 > 0):
        return False

    cross3 = compute_cross_product_scalar(line_b.start_point, line_b.end_point, line_a.start_point)
    cross4 = compute_cross_product_scalar(line_b.start_point, line_b.end_point, line_a.end_point)

    if not (cross3 > 0) ^ (cross4 > 0):
        return False

    return True


if __name__ == '__main__':
    
    while True:
        
        try:
            
            raw_input_line = raw_input()
            
            raw_values = raw_input_line.split(',')
            
            coordinates = list(map(float, raw_values))
            
            point_a = Point(coordinates[0], coordinates[1])
            point_b = Point(coordinates[2], coordinates[3])
            point_c = Point(coordinates[4], coordinates[5])
            point_d = Point(coordinates[6], coordinates[7])
            
            list_of_points = [point_a, point_b, point_c, point_d]
            
            intersection_found_flag = False
            
            for index in xrange(4):
                
                line_one = Line(list_of_points[(index + 0) % 4], list_of_points[(index + 2) % 4])
                line_two = Line(list_of_points[(index + 1) % 4], list_of_points[(index + 3) % 4])
                
                if not do_lines_intersect(line_one, line_two):
                    intersection_found_flag = True
            
            for index in xrange(4):
                
                line_one = Line(list_of_points[index], list_of_points[(index + 1) % 4])
                line_two = Line(list_of_points[(index + 2) % 4], list_of_points[(index + 3) % 4])
                
                if do_lines_intersect(line_one, line_two):
                    intersection_found_flag = True
            
            if intersection_found_flag:
                print "NO"
            else:
                print "YES"
        
        except EOFError:
            break