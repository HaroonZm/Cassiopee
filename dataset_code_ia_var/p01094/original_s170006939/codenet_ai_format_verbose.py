import collections

while True:

    total_votes_to_cast = int(input())

    if total_votes_to_cast == 0:
        break

    votes_sequence = list(input().split())

    vote_counts_per_candidate = [0] * 26

    alphabet_uppercase_letters = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]

    for vote_index, voted_candidate in enumerate(votes_sequence):

        candidate_index = alphabet_uppercase_letters.index(voted_candidate)
        vote_counts_per_candidate[candidate_index] += 1

        candidate_vote_pairs = list(zip(vote_counts_per_candidate, alphabet_uppercase_letters))

        candidate_vote_pairs_sorted = sorted(
            candidate_vote_pairs,
            key=lambda pair: -pair[0]
        )

        sorted_vote_counts, sorted_candidates = zip(*candidate_vote_pairs_sorted)
        sorted_vote_counts = list(sorted_vote_counts)
        sorted_candidates = list(sorted_candidates)

        most_votes = sorted_vote_counts[0]
        second_most_votes = sorted_vote_counts[1]

        votes_yet_to_cast = (total_votes_to_cast - vote_index - 1)

        if most_votes > (votes_yet_to_cast + second_most_votes):
            print(sorted_candidates[0], vote_index + 1)
            break

    else:
        print("TIE")