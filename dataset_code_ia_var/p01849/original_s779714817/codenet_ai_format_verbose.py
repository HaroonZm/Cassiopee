from bisect import bisect_right as bisect_right_position

def main():
    while True:
        number_of_beds, number_of_days = map(int, input().split())
        if number_of_beds == 0:
            break

        bed_comfort_values = list(map(int, input().split()))
        sorted_days_list = sorted(map(int, input().split()))

        INFINITY = 10 ** 20
        all_beds_assigned_state = 2 ** number_of_beds - 1
        memoization_scores = {}

        def compute_minimal_score(current_state_mask, accumulated_comfort, last_attended_day_index):
            if current_state_mask in memoization_scores:
                return memoization_scores[current_state_mask]
            if current_state_mask == all_beds_assigned_state:
                return 0

            selection_mask = 1
            minimal_obtained_score = INFINITY

            for bed_index in range(number_of_beds):
                if selection_mask & current_state_mask:
                    selection_mask <<= 1
                    continue

                new_accumulated_comfort = accumulated_comfort + bed_comfort_values[bed_index]
                new_state_mask = current_state_mask | selection_mask
                new_day_index = bisect_right_position(sorted_days_list, new_accumulated_comfort) - 1
                additional_score = (number_of_days - new_day_index - 1) * bed_comfort_values[bed_index]

                for day_pointer in range(last_attended_day_index + 1, new_day_index + 1):
                    if new_accumulated_comfort - sorted_days_list[day_pointer] < sorted_days_list[day_pointer] - accumulated_comfort:
                        additional_score += (sorted_days_list[day_pointer] - accumulated_comfort) - (new_accumulated_comfort - sorted_days_list[day_pointer])

                total_score = -additional_score + compute_minimal_score(new_state_mask, new_accumulated_comfort, new_day_index)
                minimal_obtained_score = min(minimal_obtained_score, total_score)

                selection_mask <<= 1

            memoization_scores[current_state_mask] = minimal_obtained_score
            return minimal_obtained_score

        total_days_sum = sum(sorted_days_list)
        minimal_score = compute_minimal_score(0, 0, -1)
        print(total_days_sum + minimal_score)

main()