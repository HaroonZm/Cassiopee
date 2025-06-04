num_balls, max_balls_to_take, num_colors = map(int, input().split())
available_colors = [int(value) for value in input().split()]
ball_list = []

for idx in range(num_balls):
    color_id, ball_value = map(int, input().split())
    ball_list.append([color_id, ball_value])

# Trier les balles par valeur décroissante
ball_list.sort(key=lambda item: item[1], reverse=True)

balls_taken_count = 0
total_value_sum = 0
current_ball_index = 0

while (balls_taken_count < max_balls_to_take) and (current_ball_index < num_balls):
    color_index = ball_list[current_ball_index][0] - 1
    if available_colors[color_index] == 0:
        current_ball_index += 1
        continue
    else:
        total_value_sum += ball_list[current_ball_index][1]
        available_colors[color_index] -= 1
        balls_taken_count += 1
        current_ball_index += 1

print(total_value_sum)