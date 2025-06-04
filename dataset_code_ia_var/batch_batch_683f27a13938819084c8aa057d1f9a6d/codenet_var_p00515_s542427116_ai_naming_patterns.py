from statistics import mean as mean_fn

input_scores_list = [int(input()) for input_index in range(5)]
adjusted_scores_list = list(map(lambda score_value: max(40, score_value), input_scores_list))
average_score_value = mean_fn(adjusted_scores_list)
print(average_score_value)