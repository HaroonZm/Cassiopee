from collections import defaultdict

while True:

    total_votes_expected = int(input())

    if total_votes_expected == 0:
        break

    vote_candidates_list = input().split()

    votes_per_candidate = defaultdict(int)
    votes_per_candidate["hoge"] = 0  # dummy entry to avoid index errors

    winner_found = False

    for current_vote_index in range(total_votes_expected):

        current_candidate = vote_candidates_list[current_vote_index]
        votes_per_candidate[current_candidate] += 1

        sorted_candidates_by_votes = sorted(
            votes_per_candidate.items(),
            key=lambda candidate_vote_pair: candidate_vote_pair[1],
            reverse=True
        )

        leading_candidate, leading_candidate_votes = sorted_candidates_by_votes[0]
        second_candidate_votes = sorted_candidates_by_votes[1][1]

        remaining_votes = total_votes_expected - 1 - current_vote_index

        if leading_candidate_votes > second_candidate_votes + remaining_votes:
            print(leading_candidate + " " + str(current_vote_index + 1))
            winner_found = True
            break

    if not winner_found:
        print("TIE")