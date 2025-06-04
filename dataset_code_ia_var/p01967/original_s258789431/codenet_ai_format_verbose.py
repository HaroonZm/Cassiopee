number_of_boxes = int(input())

box_capacity_list = list(map(int, input().split()))

number_of_queries = int(input())

query_data_list = []
for _ in range(number_of_queries):
    operation_type, box_index, operation_amount = map(int, input().split())
    query_data_list.append([operation_type, box_index, operation_amount])

apples_in_boxes = [0] * number_of_boxes

for current_query in query_data_list:
    operation_type = current_query[0]
    box_index = current_query[1]
    operation_amount = current_query[2]

    box_position = box_index - 1

    if operation_type == 1:
        apples_in_boxes[box_position] += operation_amount
        if apples_in_boxes[box_position] > box_capacity_list[box_position]:
            print(box_index)
            break
    else:
        apples_in_boxes[box_position] -= operation_amount
        if apples_in_boxes[box_position] < 0:
            print(box_index)
            break
else:
    print(0)