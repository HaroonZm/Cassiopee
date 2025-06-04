input_count = int(input())
height_list = list(map(int, input().split()))

visible_count = 0
current_max_height = 0
for height in height_list:
    if height >= current_max_height:
        visible_count += 1
        current_max_height = height

print(visible_count)