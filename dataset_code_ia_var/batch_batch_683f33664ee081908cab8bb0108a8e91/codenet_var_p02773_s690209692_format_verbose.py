number_of_candidates = int(input())

candidate_names_list = [input() for _ in range(number_of_candidates)]

import collections

candidate_vote_counter = collections.Counter(candidate_names_list)

sorted_candidate_names = sorted(candidate_vote_counter)

maximum_vote_count = max(candidate_vote_counter.values())

winning_candidates_list = []

for candidate_name, vote_count in candidate_vote_counter.items():
    if vote_count == maximum_vote_count:
        winning_candidates_list.append(candidate_name)

winning_candidates_list = sorted(winning_candidates_list)

print('\n'.join(winning_candidates_list))