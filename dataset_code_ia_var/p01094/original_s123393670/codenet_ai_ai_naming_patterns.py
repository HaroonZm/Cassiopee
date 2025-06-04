import sys
from inspect import currentframe

def debug_print(*debug_args):
    frame_vars = {id(value): name for name, value in currentframe().f_back.f_locals.items()}
    print(', '.join(frame_vars.get(id(arg), 'UNKNOWN') + ' = ' + repr(arg) for arg in debug_args))

def process_votes(num_voters, vote_list):
    ascii_A = ord('A')
    candidate_votes = [[candidate_idx, 0] for candidate_idx in range(26)]
    for voter_idx in range(num_voters):
        candidate_char = vote_list[voter_idx]
        candidate_idx = ord(candidate_char) - ascii_A
        candidate_votes[candidate_idx][1] += 1

        candidate_votes.sort(key=lambda pair: pair[1])
        if candidate_votes[-1][1] > candidate_votes[-2][1] + (num_voters - voter_idx - 1):
            winner = chr(candidate_votes[-1][0] + ascii_A)
            print(f"{winner} {voter_idx + 1}")
            return
        candidate_votes.sort(key=lambda pair: pair[0])
    print("TIE")

if __name__ == '__main__':
    while True:
        vote_count_input = int(input())
        if vote_count_input == 0:
            break
        vote_sequence_input = list(map(str, input().split()))
        process_votes(vote_count_input, vote_sequence_input)