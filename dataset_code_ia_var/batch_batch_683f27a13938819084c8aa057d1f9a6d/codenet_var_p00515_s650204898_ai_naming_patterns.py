scores_list = []
for score_index in range(5):
    current_score = int(input())
    if current_score < 40:
        current_score = 40
    scores_list.append(current_score)

average_score = sum(scores_list) // 5
print(average_score)