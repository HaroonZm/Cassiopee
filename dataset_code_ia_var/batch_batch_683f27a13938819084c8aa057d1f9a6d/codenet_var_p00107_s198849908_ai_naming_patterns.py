import math

result_list = []

while True:
    dim_depth, dim_width, dim_height = [int(token) for token in input().split(" ")]

    if dim_depth == 0 and dim_width == 0 and dim_height == 0:
        break

    calc_cheese_radius = math.sqrt((dim_width / 2) ** 2 + (dim_height / 2) ** 2)

    num_entrances = int(input())

    for entrance_index in range(num_entrances):
        val_entrance_radius = int(input())

        if calc_cheese_radius < val_entrance_radius:
            result_list.append("OK")
        else:
            result_list.append("NA")

print("\n".join(result_list))