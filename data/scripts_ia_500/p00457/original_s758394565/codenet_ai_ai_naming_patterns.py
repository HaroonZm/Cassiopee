MAX_VALUE = 100000

while True:
    element_count = int(input())
    if element_count == 0:
        break
    element_list = [int(input()) for _ in range(element_count)]

    def evaluate_position(position_index: int) -> int:
        left_color = right_color = element_list[position_index]
        left_index = right_index = position_index
        max_segment_length = 0

        for idx in range(right_index, element_count):
            if element_list[idx] != right_color:
                right_index = idx - 1
                break
        else:
            right_index = element_count - 1

        for idx in range(left_index, -1, -1):
            if element_list[idx] != left_color:
                left_index = idx + 1
                break
        else:
            left_index = 0

        if right_index - left_index - max_segment_length < 3:
            return element_count
        else:
            max_segment_length = right_index - left_index

        while left_index > 0 and right_index < element_count - 1:
            next_left_color = element_list[left_index - 1]
            next_right_color = element_list[right_index + 1]
            if next_left_color != next_right_color:
                break
            else:
                for idx in range(right_index + 1, element_count):
                    if element_list[idx] != next_right_color:
                        right_index = idx - 1
                        break
                else:
                    right_index = element_count - 1

                for idx in range(left_index - 1, -1, -1):
                    if element_list[idx] != next_left_color:
                        left_index = idx + 1
                        break
                else:
                    left_index = 0

                if right_index - left_index - max_segment_length < 4:
                    break
                else:
                    max_segment_length = right_index - left_index

        return element_count - (max_segment_length + 1)

    minimum_result = MAX_VALUE
    for position in range(element_count):
        element_list[position] = (element_list[position] + 1) % 3 + 1
        minimum_result = min(minimum_result, evaluate_position(position))
        element_list[position] = (element_list[position] + 1) % 3 + 1
        minimum_result = min(minimum_result, evaluate_position(position))
        element_list[position] = (element_list[position] + 1) % 3 + 1

    print(minimum_result)