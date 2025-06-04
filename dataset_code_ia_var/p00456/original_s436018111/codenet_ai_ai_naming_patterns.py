scores_team_w = []
scores_team_k = []

for index_input_w in range(10):
    input_score_w = int(input())
    scores_team_w.append(input_score_w)
scores_team_w.sort()
total_top3_w = scores_team_w[-1] + scores_team_w[-2] + scores_team_w[-3]

for index_input_k in range(10):
    input_score_k = int(input())
    scores_team_k.append(input_score_k)
scores_team_k.sort()
total_top3_k = scores_team_k[-1] + scores_team_k[-2] + scores_team_k[-3]

print(total_top3_w, total_top3_k)