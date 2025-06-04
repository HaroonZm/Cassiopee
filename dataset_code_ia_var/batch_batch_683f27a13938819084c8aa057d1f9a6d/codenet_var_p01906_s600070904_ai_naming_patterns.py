import math

input_n, input_m = map(int, input().split())
ball_list = list(map(int, input().split()))

lcm_nm = input_n * input_m // math.gcd(input_n, input_m)

result_sum = 0
for group_idx in range(lcm_nm // input_m):
    group_data = []
    for elem_idx in range(input_m):
        current_ball = ball_list[(group_idx * input_m + elem_idx) % len(ball_list)]
        group_data.append(current_ball)
    group_range = max(group_data) - min(group_data)
    result_sum += group_range

print(result_sum)