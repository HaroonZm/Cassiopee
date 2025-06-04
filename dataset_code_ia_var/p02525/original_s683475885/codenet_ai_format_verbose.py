import math

while True:

    number_of_scores = int(raw_input())

    if number_of_scores == 0:
        break

    scores_list = map(float, raw_input().split())

    sum_of_scores = sum(scores_list)
    mean_score = sum_of_scores / len(scores_list)

    variance_sum = 0.0

    for score_index in range(number_of_scores):
        difference = scores_list[score_index] - mean_score
        squared_difference = difference ** 2
        variance_sum += squared_difference / number_of_scores

    standard_deviation = math.sqrt(variance_sum)

    print '%.6f' % standard_deviation