import numpy as np
import sys

def main():
    input_reader = sys.stdin.read
    num_days = int(input())
    input_values = np.array(input_reader().split(), np.int32)
    contest_penalty = input_values[:26]
    satisfaction_matrix = input_values[26:].reshape((-1, 26))
    del input_values

    last_held_day = np.zeros(26)
    daily_results = []

    def select_contest_type_for_day(day_idx):
        best_score = -float('inf')
        best_type_idx = -1
        for contest_type_idx in range(26):
            selection_mask = np.ones(26)
            selection_mask[contest_type_idx] = 0
            current_score = (
                satisfaction_matrix[day_idx][contest_type_idx]
                - np.sum(contest_penalty * (day_idx + 1 - last_held_day) * selection_mask)
            )
            if current_score > best_score:
                best_score = current_score
                best_type_idx = contest_type_idx
        last_held_day[best_type_idx] = day_idx + 1
        return best_type_idx + 1, best_score

    for day_idx in range(num_days):
        contest_type, _ = select_contest_type_for_day(day_idx)
        daily_results.append(contest_type)

    print('\n'.join(map(str, daily_results)))

main()