number_of_cats = int(input())

cat_movements = list(map(int, input().split()))

cats_in_hole_stack = []

result_status = "OK"

for current_index in range(number_of_cats):

    current_movement = cat_movements[current_index]

    if current_movement < 0:

        if (len(cats_in_hole_stack) == 0 
            or current_movement != -1 * cats_in_hole_stack[-1]):

            result_status = str(current_index + 1)
            break

        else:
            cats_in_hole_stack.pop()

    else:

        if current_movement in cats_in_hole_stack:

            result_status = str(current_index + 1)
            break

        else:
            cats_in_hole_stack.append(current_movement)

print(result_status)