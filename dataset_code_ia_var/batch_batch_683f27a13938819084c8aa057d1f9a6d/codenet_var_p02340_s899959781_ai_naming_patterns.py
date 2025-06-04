import sys
input_buffer = sys.stdin.buffer.readline

def is_even_number(integer_value):
    return 1 if integer_value % 2 == 0 else 0

total_balls, total_boxes = map(int, input_buffer().split())
modulo_value = 10 ** 9 + 7

def partition_count(balls_count, boxes_count):
    dp_table = [[0] * (boxes_count + 1) for _ in range(balls_count + 1)]
    dp_table[0][0] = 1
    for balls_index in range(balls_count + 1):
        for boxes_index in range(1, boxes_count + 1):
            if boxes_index - 1 >= 0:
                dp_table[balls_index][boxes_index] += dp_table[balls_index][boxes_index - 1]
            if balls_index - boxes_index >= 0:
                dp_table[balls_index][boxes_index] += dp_table[balls_index - boxes_index][boxes_index]
            dp_table[balls_index][boxes_index] %= modulo_value
    return dp_table[balls_count][boxes_count]

print(partition_count(total_balls, total_boxes))