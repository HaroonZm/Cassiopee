import collections

while True:
    candidate_count = int(input())
    if candidate_count == 0:
        break

    ballot_inputs = list(input().split())
    vote_counts = [0] * 26
    candidate_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for ballot_index, ballot_choice in enumerate(ballot_inputs):
        candidate_pos = candidate_labels.index(ballot_choice)
        vote_counts[candidate_pos] += 1

        merged_votes = list(zip(vote_counts, candidate_labels))
        merged_votes_sorted = sorted(merged_votes, key=lambda pair: -pair[0])
        sorted_vote_counts, sorted_candidate_labels = zip(*merged_votes_sorted)
        vote_counts = list(sorted_vote_counts)
        candidate_labels = list(sorted_candidate_labels)

        if vote_counts[0] > (candidate_count - ballot_index - 1) + vote_counts[1]:
            print(candidate_labels[0], ballot_index + 1)
            break
    else:
        print("TIE")