while True:
    num_votes = int(input())
    if num_votes == 0:
        break
    votes_list = input().split()
    candidate_counts = {}
    winner_vote_count = 0
    runnerup_vote_count = 0
    winner_candidate = None
    winner_found = False
    for vote_index, candidate in enumerate(votes_list):
        if candidate not in candidate_counts:
            candidate_counts[candidate] = 1
        else:
            candidate_counts[candidate] += 1
        
        max_count = 0
        second_max_count = 0
        max_candidate = None
        for current_candidate in candidate_counts:
            current_count = candidate_counts[current_candidate]
            if current_count > max_count:
                second_max_count = max_count
                max_count = current_count
                max_candidate = current_candidate
            elif current_count > second_max_count:
                second_max_count = current_count
        
        if max_count - second_max_count > num_votes - (vote_index + 1):
            print(max_candidate, vote_index + 1)
            winner_found = True
            break
    if not winner_found:
        if max_count == second_max_count:
            print('TIE')