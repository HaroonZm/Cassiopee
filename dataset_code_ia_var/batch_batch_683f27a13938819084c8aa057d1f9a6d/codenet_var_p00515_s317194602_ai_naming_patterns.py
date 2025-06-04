total_score = 0
for idx_score_input in range(5):
    current_score_raw = int(input())
    current_score_adjusted = max(40, current_score_raw)
    current_score_contribution = current_score_adjusted // 5
    total_score += current_score_contribution
print(total_score)