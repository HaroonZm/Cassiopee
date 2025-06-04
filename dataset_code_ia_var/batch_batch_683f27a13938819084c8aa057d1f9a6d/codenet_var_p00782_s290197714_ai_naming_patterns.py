import sys

def rectangle_is_contained(rect_a, rectangles_list):
    rect_a_x1, rect_a_y1, rect_a_x2, rect_a_y2 = rect_a
    for rect_b in rectangles_list:
        rect_b_x1, rect_b_y1, rect_b_x2, rect_b_y2 = rect_b
        if rect_b_x1 <= rect_a_x1 <= rect_b_x2 and rect_b_x1 <= rect_a_x2 <= rect_b_x2 and \
           rect_b_y1 <= rect_a_y1 <= rect_b_y2 and rect_b_y1 <= rect_a_y2 <= rect_b_y2:
            return True
    return False

def rectangle_list_add(rect_to_add, rectangles_list):
    if rectangle_is_contained(rect_to_add, rectangles_list):
        return rectangles_list
    add_x1, add_y1, add_x2, add_y2 = rect_to_add
    if add_x1 >= add_x2 or add_y1 >= add_y2:
        return rectangles_list
    result_list = rectangles_list
    if rectangles_list == []:
        return [rect_to_add]
    temp_split_list = []
    for rect_existing in rectangles_list:
        ex_x1, ex_y1, ex_x2, ex_y2 = rect_existing
        if add_x1 < ex_x1 < add_x2 and add_y1 < ex_y1 < add_y2 and add_x2 <= ex_x2 and add_y2 <= ex_y2:
            temp_split_list = [[add_x1, add_y1, add_x2, ex_y1], [add_x1, ex_y1, ex_x1, add_y2]]
        elif add_x1 < ex_x1 < add_x2 and add_y1 < ex_y2 < add_y2 and ex_y1 <= add_y1 and add_x2 <= ex_x2:
            temp_split_list = [[add_x1, add_y1, ex_x1, ex_y2], [add_x1, ex_y2, add_x2, add_y2]]
        elif add_x1 < ex_x2 < add_x2 and add_y1 < ex_y1 < add_y2 and ex_x1 <= add_x1 and add_y2 <= ex_y2:
            temp_split_list = [[add_x1, add_y1, ex_x2, ex_y1], [ex_x2, add_y1, add_x2, add_y2]]
        elif add_x1 < ex_x2 < add_x2 and add_y1 < ex_y2 < add_y2 and ex_x1 <= add_x1 and ex_y1 <= add_y1:
            temp_split_list = [[add_x1, ex_y2, ex_x2, add_y2], [ex_x2, add_y1, add_x2, add_y2]]
        elif add_x1 < ex_x1 and add_y1 <= ex_y1 < add_y2 and ex_x2 < add_x2 and add_y2 <= ex_y2:
            temp_split_list = [[add_x1, add_y1, add_x2, ex_y1], [add_x1, ex_y1, ex_x1, add_y2], [ex_x2, ex_y1, add_x2, add_y2]]
        elif add_x1 < ex_x1 and add_y1 < ex_y2 <= add_y2 and ex_x2 < add_x2 and ex_y1 <= add_y1:
            temp_split_list = [[add_x1, ex_y2, add_x2, add_y2], [add_x1, add_y1, ex_x1, ex_y2], [ex_x2, add_y1, add_x2, ex_y2]]
        elif add_x1 <= ex_x1 < add_x2 and add_y1 < ex_y1 and ex_y2 < add_y2 and add_x2 <= ex_x2:
            temp_split_list = [[add_x1, add_y1, ex_x1, add_y2], [ex_x1, add_y1, add_x2, ex_y1], [ex_x1, ex_y2, add_x2, add_y2]]
        elif add_x1 < ex_x2 <= add_x2 and add_y1 < ex_y1 and ex_y2 < add_y2 and ex_x1 <= add_x1:
            temp_split_list = [[ex_x2, add_y1, add_x2, add_y2], [add_x1, add_y1, ex_x2, ex_y1], [add_x1, ex_y2, ex_x2, add_y2]]
        elif ex_x1 <= add_x1 and add_x2 <= ex_x2 and add_y1 < ex_y1 < add_y2 and add_y2 <= ex_y2:
            temp_split_list = [[add_x1, add_y1, add_x2, ex_y1]]
        elif ex_y1 <= add_y1 and add_y2 <= ex_y2 and add_x1 < ex_x1 < add_x2 and add_x2 <= ex_x2:
            temp_split_list = [[add_x1, add_y1, ex_x1, add_y2]]
        elif ex_x1 <= add_x1 and add_x2 <= ex_x2 and add_y1 < ex_y2 < add_y2 and ex_y1 <= add_y1:
            temp_split_list = [[add_x1, ex_y2, add_x2, add_y2]]
        elif ex_y1 <= add_y1 and add_y2 <= ex_y2 and add_x1 < ex_x2 < add_x2 and ex_x1 <= add_x1:
            temp_split_list = [[ex_x2, add_y1, add_x2, add_y2]]
        elif add_x1 < ex_x1 < add_x2 and add_x1 < ex_x2 < add_x2 and add_y1 < ex_y1 < add_y2 and add_y1 < ex_y2 < add_y2:
            temp_split_list = [[add_x1, add_y1, ex_x1, ex_y2], [add_x1, ex_y2, ex_x2, add_y2], [ex_x2, ex_y1, add_x2, add_y2], [ex_x1, add_y1, add_x2, ex_y1]]
        elif ex_x1 <= add_x1 and add_x2 <= ex_x2 and add_y1 < ex_y1 and ex_y2 < add_y2:
            temp_split_list = [[add_x1, add_y1, add_x2, ex_y1], [add_x1, ex_y2, add_x2, add_y2]]
        elif ex_y1 <= add_y1 and add_y2 <= ex_y2 and add_x1 < ex_x1 and ex_x2 < add_x2:
            temp_split_list = [[add_x1, add_y1, ex_x1, add_y2], [ex_x2, add_y1, add_x2, add_y2]]
        if temp_split_list != []:
            for rect_split in temp_split_list:
                result_list = rectangle_list_add(rect_split, result_list)
            break
    if temp_split_list == []:
        result_list.append(rect_to_add)
    return result_list

def rectangle_list_area(rectangles_list):
    area_sum = 0.0
    for rect in rectangles_list:
        area_sum += (rect[2] - rect[0]) * (rect[3] - rect[1])
    return area_sum

testcase_count = 0
rectangle_count = 0
rectangles_main = []
for input_line in sys.stdin:
    if testcase_count == 0:
        testcase_count = int(input_line)
        rectangle_count += 1
        rectangles_main = []
        if testcase_count == 0:
            break
    else:
        point_data = list(map(float, input_line.strip().split()))
        single_rect = [point_data[0] - point_data[2], point_data[1] - point_data[2], point_data[0] + point_data[2], point_data[1] + point_data[2]]
        rectangles_main = rectangle_list_add(single_rect, rectangles_main)
        testcase_count -= 1
        if testcase_count == 0:
            print("%d %.2f" % (rectangle_count, rectangle_list_area(rectangles_main)))