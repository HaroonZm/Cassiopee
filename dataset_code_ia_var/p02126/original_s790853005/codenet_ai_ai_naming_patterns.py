num_balls, max_picks, num_colors = map(int, input().split())
balls_available_per_color = list(map(int, input().split()))
balls_info = [list(map(int, input().split())) for _ in range(num_balls)]
balls_info.sort(key=lambda ball: ball[1], reverse=True)
total_weight = 0
for ball_color, ball_weight in balls_info:
    color_idx = ball_color - 1
    if balls_available_per_color[color_idx]:
        total_weight += ball_weight
        balls_available_per_color[color_idx] -= 1
        max_picks -= 1
        if max_picks == 0:
            break
print(total_weight)