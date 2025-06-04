list_team_a_scores = []
list_team_b_scores = []

for idx_team_a_input in range(10):
    list_team_a_scores.append(int(input()))
for idx_team_b_input in range(10):
    list_team_b_scores.append(int(input()))

list_team_a_scores.sort(reverse=True)
list_team_b_scores.sort(reverse=True)

int_team_a_top3_sum = sum(list_team_a_scores[:3])
int_team_b_top3_sum = sum(list_team_b_scores[:3])

print(int_team_a_top3_sum, int_team_b_top3_sum)