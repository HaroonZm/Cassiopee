import sys

from inspect import currentframe

def print_variable_names_and_values(*variable_arguments):
    variable_names_dict = {id(variable_value): variable_name for variable_name, variable_value in currentframe().f_back.f_locals.items()}
    print(', '.join(variable_names_dict.get(id(argument), '???') + ' = ' + repr(argument) for argument in variable_arguments))

def determine_election_winner(total_votes, votes_sequence):
    ascii_offset_for_A = ord("A")
    candidate_vote_counts = [[candidate_index, 0] for candidate_index in range(26)]
    
    for current_vote_index in range(total_votes):
        current_vote_char = votes_sequence[current_vote_index]
        candidate_index = ord(current_vote_char) - ascii_offset_for_A
        candidate_vote_counts[candidate_index][1] += 1

        candidate_vote_counts.sort(key=lambda candidate_data: candidate_data[1])

        votes_leading_candidate = candidate_vote_counts[-1][1]
        votes_runner_up = candidate_vote_counts[-2][1]
        votes_remaining = total_votes - current_vote_index - 1

        if votes_leading_candidate > votes_runner_up + votes_remaining:
            winning_candidate_character = chr(candidate_vote_counts[-1][0] + ascii_offset_for_A)
            print(winning_candidate_character + " " + str(current_vote_index + 1))
            return
        
        candidate_vote_counts.sort()
    
    print("TIE")
    return

if __name__ == '__main__':
    while True:
        number_of_votes = int(input())
        if number_of_votes == 0:
            break

        votes_input_list = list(map(str, input().split()))
        determine_election_winner(number_of_votes, votes_input_list)