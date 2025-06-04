from bisect import bisect_right

rect_data_list = [(rect_h ** 2 + rect_w ** 2, rect_h, rect_w) for rect_h in range(1, 151) for rect_w in range(1, 151) if rect_h < rect_w]
rect_data_list.sort()

while True:
    input_h, input_w = map(int, input().split())
    if input_h == 0 and input_w == 0:
        break

    input_key = (input_h ** 2 + input_w ** 2, input_h, input_w)
    next_rect_index = bisect_right(rect_data_list, input_key)
    next_rect = rect_data_list[next_rect_index]
    print(next_rect[1], next_rect[2])