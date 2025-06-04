input_length = int(input())
height_list = list(map(int, input().split()))
visible_count = 1
current_max_height = height_list[0]
for index in range(1, input_length):
    if height_list[index] >= current_max_height:
        visible_count += 1
        current_max_height = max(current_max_height, height_list[index])
print(visible_count)