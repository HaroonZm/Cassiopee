while True:
    total_number_of_votes = int(input())

    if total_number_of_votes == 0:
        break

    list_of_vote_choices = [vote_choice for vote_choice in input().split()]

    vote_counts_by_candidate = {}

    winner_vote_count = 0
    runnerup_vote_count = 0
    current_winner_candidate = None

    for current_vote_index, current_candidate in enumerate(list_of_vote_choices):

        if current_candidate not in vote_counts_by_candidate:
            vote_counts_by_candidate[current_candidate] = 1
        else:
            vote_counts_by_candidate[current_candidate] += 1

        winner_vote_count = 0
        runnerup_vote_count = 0
        current_winner_candidate = None

        for candidate_name in vote_counts_by_candidate:
            candidate_vote_count = vote_counts_by_candidate[candidate_name]
            if candidate_vote_count > winner_vote_count:
                runnerup_vote_count = winner_vote_count
                winner_vote_count = candidate_vote_count
                current_winner_candidate = candidate_name
            elif candidate_vote_count > runnerup_vote_count:
                runnerup_vote_count = candidate_vote_count

        remaining_votes = total_number_of_votes - (current_vote_index + 1)
        if winner_vote_count - runnerup_vote_count > remaining_votes:
            print(current_winner_candidate, current_vote_index + 1)
            break

    if winner_vote_count == runnerup_vote_count:
        print('TIE')