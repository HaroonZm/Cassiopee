input_count = int(input())
height_list = list(map(int, input().split()))
current_max_height = height_list[0]
visible_count = 1
for index in range(1, input_count):
    if height_list[index] >= current_max_height:
        visible_count += 1
        current_max_height = height_list[index]
print(visible_count)