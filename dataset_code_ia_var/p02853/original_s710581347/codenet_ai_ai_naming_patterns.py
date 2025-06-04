input_x, input_y = map(int, input().split())
total_score = 0
if 1 <= input_x <= 3:
    total_score += (4 - input_x) * 10**5
if 1 <= input_y <= 3:
    total_score += (4 - input_y) * 10**5
if input_x == 1 and input_y == 1:
    total_score += 4 * 10**5
print(total_score)