number_of_candidates, number_of_judges = map(int, raw_input().split())

candidate_scores_and_judge_scores = [input() for candidate_or_judge_index in range(number_of_candidates + number_of_judges)]

candidate_votes = [0] * number_of_candidates

for judge_index in range(number_of_candidates, number_of_candidates + number_of_judges):
    
    for candidate_index in range(number_of_candidates):
        
        if candidate_scores_and_judge_scores[judge_index] >= candidate_scores_and_judge_scores[candidate_index]:
            
            candidate_votes[candidate_index] += 1
            
            break

index_of_candidate_with_most_votes = candidate_votes.index(max(candidate_votes)) + 1

print index_of_candidate_with_most_votes